#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：数据处理
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : main.py
@创建时间：2018/6/15 13:26
'''
from file_data import data_all
from database import Access
from database import session

for k,v in data_all.items():
    print("开始插入。。。")
    access_ = Access(ip_address=v["ip_address"])
    # access_ = Access(ip_address=v["ip_address"].strip(), sys_time=str(v["sys_time"]).strip(), visit_time=str(v["visit_time"]).strip(), report_type=str(v["report_type"]).strip(),
    #                  visitor_type=str(v["visitor_type"]).strip(), user_id=v["user_id"].strip(),  account_name=v["account_name"].strip(),
    #                  phone_number=str(v["phone_number"]).strip(), os=v["os"], browser=v["browser"].strip(), mac_address=v["mac_address"].strip(),
    #                  app_version=v["app_version"].strip(), visit_url=v["visit_url"].strip(), detail=v["detail"].strip())
    session.add(access_)
    session.commit()
    print("插入成功。。。")