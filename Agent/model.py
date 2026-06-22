# ========================================
# 导入模型初始化所需的最小依赖
# ========================================
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# ========================================
# 初始化 DeepSeek V4 Flash 模型（关闭思考模式，兼容最广）
# ========================================
llm = ChatOpenAI(
    model="deepseek-v4-flash",
    openai_api_key=os.environ["DEEPSEEK_API_KEY"],  # 环境变量获取，不硬编码
    openai_api_base="https://api.deepseek.com/v1",
    temperature=0,
    max_tokens=8000,
    extra_body={"thinking": {"type": "disabled"}},
)

# ========================================
# 验证连通性
# ========================================
try:
    llm.invoke([HumanMessage(content="hello world")])
    print("[OK] DeepSeek V4 Flash ready")
except Exception:
    print("[WARN] model connect failed, check DEEPSEEK_API_KEY")