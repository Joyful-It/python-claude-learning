from sqlalchemy.orm import create_engine
from sqlalchemy.orm import sessionmaker
"""
数据库连接工具
from sqlalchemy import create_engine           # 创建数据库连接的工具
from sqlalchemy.orm import sessionmaker        # 创建会话的工具

sqlalchemy.orm 是ORM工具箱,提供数据库会话管理功能。
将数据库操作封装成Python对象方便开发。将数据库表映射为Python类。
SELECT * FROM t_emp    db.query(Emp).all()
INSERT INTO ...        db.add(emp)         一一对应
"""




engine = create_engine("mysql+pymysql://root:123456@localhost:3306/emp", echo=True)

"""
mysql+pymysql://   ← 用 pymysql 这个驱动连接 MySQL 数据库
root               ← 用户名
:xing%401688       ← 密码（@前面是用户名，:后面是密码）
@127.0.0.1:3306    ← 数据库地址和端口(127.0.0.1 = 本机)
/db_company        ← 数据库名字

mysql
固定的数据库方言标识，告诉程序：我要连接的是 MySQL 数据库。
(换数据库就改这里:postgresql、sqlite、oracle、sqlserver)
+
固定分隔符<专门用来分隔「数据库类型」和「Python 驱动」，必须这么写。
pymysql
Python 连接 MySQL 的底层驱动（负责真正和 MySQL 服务器通信）。
✅ 这部分不是唯一固定的，可以替换成其他合法驱动。
"""



sessionLocal = sessionmaker(bind=engine)
"""
sessionmaker  # 这是一个"类"，就像一个说明书
sessionmaker(bind=engine)  # 这才是创建一个"实例"，一台真正的机器  
"""