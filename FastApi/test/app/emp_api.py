# emp = Emp(name="张三", age=25, job="工程师")  # 1. 创建对象
# db.add(emp)     # 2. 放入暂存区（还没真正保存）
# db.commit()     # 3. 确认保存（真正写入数据库）
import datetime

from fastapi import APIRouter,Depends
from pydantic import BaseModel,Field
from sqlalchemy.orm import session
from schemas.datamodel import Emp      # 导入 Emp 类（后面讲）
from schemas.dbutil import sessionLocal # 导入数据库连接工具
'''import datetime              # 导入日期时间模块（处理创建时间）
from fastapi import APIRouter, Depends  # 导入路由和依赖注入
from pydantic import BaseModel, Field   # 导入数据验证工具
from sqlalchemy.orm import session      # 导入数据库会话类型
from schemas.datamodel import Emp      # 导入 Emp 类（后面讲）
from schemas.dbutil import sessionLocal # 导入数据库连接工具
'''

router=APIRouter(prefix="/love",tags=["like"])

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
函数文档字符串：
◦ 说明函数的核心功能：作为 FastAPI 依赖注入系统的一部分，为 API 请求提供数据库会话
◦ 解释实现机制：采用生成器模式和 try-finally 结构，确保会话在使用后正确关闭
◦ 明确返回值：生成数据库会话对象的生成器，供依赖此函数的 API 端点使用
2. 行内注释：
◦ 对 db = sessionLocal() 的注释：创建数据库会话实例
◦ 对 yield db 的注释：生成会话对象，供依赖此函数的 API 端点使用
◦ 对 db.close() 的注释：确保无论是否发生异常，都会关闭数据库会话，避免连接泄漏
"""
class EmpAdd(BaseModel):
    name: str = Field(min_length=2, max_length=10, description="员工姓名")
    age: int = Field(ge=12,le=20, description="员工年龄")
    job: str = Field(min_length=2, max_length=20, description="员工岗位")
"""
1**数值类型(int, float)**的验证参数：
◦ (ge)：大于等于
◦ (le)：小于等于
◦ (gt)：大于
◦ (lt)：小于
◦ (multiple_of)：必须是某个数的倍数
2. **字符串类型(str)**的验证参数：
◦ (min_length)：最小长度
◦ (max_length)：最大长度
◦ (regex)：正则表达式匹配
◦ (strip_whitespace)：自动去除首尾空格
3. 其他类型的参数：
◦ (default)：默认值
◦ (description)：字段描述(用于API文档  )
◦ (alias)：字段别名
◦ (required)：是否必填(默认True)
"""
