#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：PyCharm
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : file_data.py
@创建时间：2018/6/15 13:21
'''
import re

data_all = {}
data_ev = {}

print("开始提取。。。")
with open("sample.log") as f:
    count = 1
    for line in f.readlines():
            ip_address = ''
            sys_time = ''
            visit_time = ''
            report_type = ''
            visitor_typ = ''
            user_id = ''
            account_name =''
            phone_number = ''
            os = ''
            app_version = ''
            detail = ''
            visit_url = ''
            browser = ''
            mac_address = ''
            visitor_type = ''
            if 'ip_address' in line:
                if line is not None:
                   ip_address = line.strip().split('ip_address:')[1]
                else:
                    print ''
                data_ev['ip_address'] = ip_address
            if 'sys_time' in line:
                if line is not None:
                    sys_time = line.strip().split('sys_time:')[1]
                else:
                    print ''
                data_ev['sys_time'] = sys_time
            if 'report_type' in line:
                if line is not None:
                    report_type = line.strip().split('report_type:')[1]
                else:
                    print ''
                data_ev['report_type'] = report_type
            if 'visit_time' in line:
                if line is not None:
                    visit_time = line.strip().split('visit_time:')[1]
                else:
                    print ''
                data_ev['visit_time'] = visit_time
            if 'visitor_type' in line:
                if line is not None:
                    visitor_type = line.strip().split('visitor_type:')[1]
                else:
                    print ''
                data_ev['visitor_type'] = visitor_type
            if 'user_id' in line:
                if line is not None:
                     user_id = line.strip().split('user_id:')[1]
                else:
                    print ''
                data_ev['user_id'] = user_id
            if 'account_name' in line:
                if line is not None:
                    account_name = line.strip().split('account_name:')[1]
                else:
                    print ''
                data_ev['account_name'] = account_name
            if 'phone_number' in line:
                if line is not None:
                    print line.strip().split('phone_number:')[1]
                else:
                    print ''
                data_ev['phone_number'] = phone_number
            if 'os' in line:
                if line is not None:
                    print line.strip().split('os:')[1]
                else:
                    print ''
                data_ev['os'] = os
            if 'browser' in line:
                if line is not None:
                    browser= line.strip().split('browser:')[1]
                else:
                    print ''
                data_ev['browser'] = browser
            if 'mac_address' in line:
                if line is not None:
                    mac_address = line.strip().split('mac_address:')[1]
                else:
                    print ''
                data_ev['mac_address'] = mac_address
            if 'app_version' in line:
                if line is not None:
                    app_version =  line.strip().split('app_version:')[1]
                else:
                    print ''
                data_ev['app_version'] = app_version
            if 'visit_url' in line:
                if line is not None:
                    visit_url = line.strip().split('visit_url:')[1]
                else:
                     print ''
                data_ev['visit_url'] = visit_url
            if 'detail' in line:
                if line is not None:
                    detail = line.strip().split('detail:')[1]
                else:
                    print ''
                data_ev['detail'] = detail
                print('kk', data_ev)
            data_all[count] = data_ev

            print("已完成"+str(count)+"行。。。")
            #count += 1
                #reg = re.compile('^(?P<remote_ip>[^ ]*) (?P<date>[^ ]*) "(?P<request>[^"]*)" (?P<status>[^ ]*) (?P<size>[^ ]*) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"')
                #reg = re.compile('^(?P<ip_address>[^ ]*)')
               # regMatch = re.search(r.'PY.*?N',line)
                #linebits = regMatch.groupdict()
                #print linebits
                #for k, v in linebits.items():
                    #print k+": "+v

            #
            # line = line.strip('\n')
            # line = re.split("\s|-", line)
            # print(line)
            # data_ev["ip_address"] = line[0]
            # data_ev["sys_time"] = line[5].split('[')[1]
            # data_ev["visit_time"] = line[7].split('"')[1]
            # data_ev["url"] = line[8]
            # data_ev["http_status"] = line[9]
            # if line[10] == '-':
            #     data_ev["body_bytes_sent"] = 0
            # else:
            #     data_ev["body_bytes_sent"] = line[10]
            # data_ev["http_referer"] = line[11].split('"')
            # data_ev["ua"] = ' '.join(line[12:23]).split('"')
            # if data_ev["http_method"] == 'GET':
            #     data_ev["ua"] = data_ev["ua"][3]
            # else:
            #     data_ev["ua"] = data_ev["ua"][1] + data_ev["ua"][3]
            # print(data_ev)
            # data_all[count] = data_ev
            # # print("已完成"+count+"行。。。")
            # count += 1