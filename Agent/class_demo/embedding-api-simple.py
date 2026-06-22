"""
简化版 Embedding API - 使用原生 Transformers/Sentence-Transformers
适合教学演示，代码结构清晰简单
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import torch
import numpy as np

app = FastAPI()

# ============ 模型加载 ============
# 直接使用 SentenceTransformer 加载本地模型
# 会自动处理 tokenizer 和模型的加载
model_path = './bge-m3'
device = 'cuda' if torch.cuda.is_available() else 'cpu'

print(f"正在加载模型: {model_path}")
print(f"使用设备: {device}")

# 加载模型（会自动使用 GPU 如果可用）
model = SentenceTransformer(model_path, device=device)
print("模型加载成功！")

# ============ 数据模型定义 ============
class EmbeddingRequest(BaseModel):
    """请求体结构"""
    model: str          # 模型名称（预留字段）
    input: list[str]    # 要编码的文本列表
    dimensions: int     # 向量维度（预留字段）
    sparse: bool = False  # 是否返回稀疏向量（本简化版不支持）


class EmbeddingResponse(BaseModel):
    """响应体结构"""
    model: str
    data: list[dict]
    usage: dict

# ============ 核心功能 ============
def compute_embeddings(texts: list[str], batch_size: int = 8):
    """
    计算文本的 embedding 向量
    
    Args:
        texts: 要编码的文本列表
        batch_size: 批处理大小
    
    Returns:
        embeddings: numpy 数组，shape = (len(texts), 向量维度)
    """
    if not texts:
        raise ValueError("输入文本不能为空")
    
    # SentenceTransformer 会自动处理:
    # 1. Tokenization（分词）
    # 2. Model inference（模型推理）
    # 3. Pooling（池化）
    # 4. Normalization（归一化）
    embeddings = model.encode(
        texts, 
        batch_size=batch_size,
        convert_to_numpy=True,      # 返回 numpy 数组
        normalize_embeddings=True,   # L2 归一化
        show_progress_bar=False
    )
    
    return embeddings

# ============ API 路由 ============
@app.post("/v1/embeddings")
def embedding(req: EmbeddingRequest):
    """
    Embedding 接口 - 兼容 OpenAI API 格式
    
    示例请求:
    {
        "model": "bge-m3",
        "input": ["这是一段测试文本", "这是另一段文本"],
        "dimensions": 1024
    }
    """
    try:
        # 1. 计算 embedding
        embeddings = compute_embeddings(req.input)
        
        # 2. 构造返回数据
        data = []
        for i, emb in enumerate(embeddings):
            data.append({
                "object": "embedding",
                "index": i,
                "embedding": emb.tolist()  # numpy 转 list
            })
        
        # 3. 构造 usage 信息（简单估算 token 数）
        # 粗略估计：1个汉字 ≈ 1.5 个 token，1个英文单词 ≈ 1 个 token
        total_chars = sum(len(text) for text in req.input)
        estimated_tokens = int(total_chars * 0.75)  # 粗略估算
        
        return EmbeddingResponse(
            model=req.model,
            data=data,
            usage={
                "prompt_tokens": estimated_tokens,
                "total_tokens": estimated_tokens
            }
        )
        
    except Exception as e:
        print(f"处理请求时出错: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/info/models")
def model_info():
    """获取模型信息"""
    return {
        "model_name": "bge-m3",
        "model_path": model_path,
        "device": device,
        "vector_dimensions": model.get_sentence_embedding_dimension(),
        "max_seq_length": model.max_seq_length,
        "description": "BGE-M3 是 BAAI 开源的多语言 Embedding 模型",
        "features": [
            "支持 100+ 种语言",
            "支持长文本（最大 8192 tokens）",
            "同时支持稠密向量（Dense）和稀疏向量（Sparse）",
            "支持多任务（检索、排序、分类等）"
        ],
        "note": "本简化版只支持稠密向量（Dense Embedding）"
    }

@app.get("/health")
def health_check():
    """健康检查接口"""
    return {
        "status": "ok",
        "model_loaded": model is not None,
        "device": device,
        "cuda_available": torch.cuda.is_available()
    }

# ============ 启动服务 ============
if __name__ == "__main__":
    import uvicorn
    
    print("\n" + "="*50)
    print("简化版 Embedding API 服务启动")
    print("="*50)
    print(f"接口地址: http://localhost:8999")
    print(f"API 文档: http://localhost:8999/docs")
    print(f"模型维度: {model.get_sentence_embedding_dimension()}")
    print(f"运行设备: {device}")
    print("="*50 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8999, log_level="info")
