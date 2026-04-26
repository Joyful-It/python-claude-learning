import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
"""
Column:
◦ 用于定义数据库表中的列
◦ 是 SQLAlchemy 中最基本的构建块
◦ 每个数据库字段都需要使用 Column 来定义
2. Integer:
◦ 数据类型：表示整数类型的列
◦ 对应数据库中的 INT 类型
◦ 常用于 ID、年龄等整数值
3. String:
◦ 数据类型：表示字符串类型的列
◦ 对应数据库中的 VARCHAR 类型
◦ 常用于姓名、岗位等文本值
4. DateTime:
◦ 数据类型：表示日期时间类型的列
◦ 对应数据库中的 DATETIME 类型
◦ 常用于创建时间、更新时间等时间值
5. ForeignKey:
◦ 用于定义外键关系
◦ 建立表与表之间的关联
◦ 确保数据的完整性和一致性
"""
from schems.dbuilt import engine

Base = declarative_base()
class