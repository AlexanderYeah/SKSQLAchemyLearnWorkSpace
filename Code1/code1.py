#coding=utf-8;

import sqlalchemy

from sqlalchemy import *
from sqlalchemy.orm import  *
from sqlalchemy.ext.declarative import  *

import pymysql

# 创建对象的基类
Base = declarative_base();


class User(Base):
    # 表的名字
    __tablename__ = 'user';
    # 表的结构
    id = Column(String(20),primary_key=True);
    name = Column(String(20));


# 0 初始化数据库的连接
#  '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test');

# 1 创建DBSession 类型
DBSession = sessionmaker(bind=engine);

# 以上的代码用来初始化数据库的连接


# 进行添加一行的操作  所谓session 就是当前数据库的连接
# 0 实例化session
session = DBSession();
# 1 创建新的USER对象
new_user = User(id = '1',name='YEAH');
#2 添加到session
session.add(new_user);
#3 提交保存到数据库
session.commit();
#4 关闭session
session.close();






