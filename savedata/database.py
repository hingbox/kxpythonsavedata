#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：PyCharm
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : database.py
@创建时间：2018/6/15 13:22
'''
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from file_data import data_all

BaseModel = declarative_base()
print("开始连接数据库。。。")
DB_CONNECT = 'mysql+pymysql://root:root@localhost:3306/test'
engine = create_engine(DB_CONNECT, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
print("连接成功。。。")

class Access(BaseModel):
    print("111")
    __tablename__ = 't_report'
    id = Column(Integer(), primary_key=True)
    ip_address = Column(String(50))
    sys_time = Column(String(50))
    account_name = Column(String(50))
    visit_time = Column(String(50))
    visitor_type = Column(String(50))
    report_type = Column(String(50))
    user_id = Column(String(50))
    phone_number = Column(String(50))
    os = Column(String(50))
    browser = Column(String(50))
    mac_address = Column(String(50))
    app_version = Column(String(50))
    visit_url = Column(String(225))
    detail = Column(String(500))

#created	datetime	0	0	-1	0	0	0	0		0	创建时间				0	0


def init_db():
    BaseModel.metadata.create_all(engine)
def drop_db():
    BaseModel.metadata.drop_all(engine)

# drop_db()
# init_db()