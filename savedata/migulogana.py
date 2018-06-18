#!/usr/bin/python
#coding:utf8
import threading
import time
import os
import shutil
import re
import csv
fuhao=os.linesep
start_time=int(time.strftime('%H%M%S'))
print start_time
def count_cpu_heshu():
    file=open('/proc/cpuinfo')
    cpu_sum=[]
    for line in file.readlines():
        cpu_he=re.findall('^processor',line)
        if len(cpu_he)==1:
           cpu_sum.append(cpu_he)
        else:
           continue
    file.close()
    return len(cpu_sum)
def count_memory_size():
    mem_sum=int(os.popen("free -m|awk  '{print $2}'|sed -n '2p'").readline().strip())
    return mem_sum


def analyse(logfilename,reportfilename):
    acnum=[];time_res=[];lnum=0
    file=open(logfilename)
    destfile=open(reportfilename, 'a')
    csv.register_dialect("pipes", delimiter="|")
    csv_write = csv.writer(destfile,delimiter="|")
    #sizehint=int(count_memory_size() / count_cpu_heshu() * 0.5 * 1024 * 1024)
    position=0
    tmpstartline = 0
    tmpstartline = 0
    names =["ip_address","sys_time","report_type","visit_time","visitor_type","user_id","account_name","phone_number","os","browser","mac_address","app_version","visit_url"]

    linedict = {"recordtime":"","ip_address":"","sys_time":"","report_type":"","visit_time":"","visitor_type":"","user_id":"","account_name":"","phone_number":"","os":"","browser":"","mac_address":"","app_version":"","visit_url":""}

    csv_write.writerow(names)

    for (num,line) in enumerate(file):
        if(re.search(r'^(.*)====\[report begin\]====(.*)$',line)):
            #/[INFO] 2018-06-14 22:23:49
            date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})",line)
            print date_all[0]
            tmpstartline = 1
            linedict["recordtime"] = date_all[0]
            linedict["ip_address"] = ""
            linedict["sys_time"] = ""
            linedict["report_type"] = ""
            linedict["visit_time"] = ""
            linedict["visitor_type"] = ""
            linedict["user_id"] = ""
            linedict["account_name"] = ""
            linedict["phone_number"] = ""
            linedict["os"] = ""
            linedict["browser"] = ""
            linedict["mac_address"] = ""
            linedict["app_version"] = ""
            linedict["visit_url"] = ""
            #print "begin line"
        elif(re.search(r'^(.*)====\[report end\]====(.*)$',line)):
            tmpstartline = 0
            #save line and reset
            tmpvals = [
            linedict["ip_address"] ,
            linedict["sys_time"] ,
            linedict["report_type"] ,
            linedict["visit_time"] ,
            linedict["visitor_type"],
            linedict["user_id"] ,
            linedict["account_name"],
            linedict["phone_number"] ,
            linedict["os"] ,
            linedict["browser"] ,
            linedict["mac_address"] ,
            linedict["app_version"] ,
            linedict["visit_url"] ]
            #print tmpvals
            csv_write.writerow(tmpvals)
            #print "end line"
        elif tmpstartline == 1:
            for name in names:
                if(re.search(r"^(.*)"+name+"(.*)$", line)):
                    tmpindex = line.find(name+":")
                    if tmpindex !=-1:
                        tmpindex = tmpindex+ len(name)+1
                        #print name," is ",line[tmpindex:]
                        linedict[name] = line[tmpindex:len(line)-1].strip()
    file.close()
    destfile.close()

if __name__ == '__main__':
    #analyse("d:/sample.log","d:/sample.csv")
    #analyse("D:/temp/176_20180614/MiguApi__2018-06-14.log");
    #analyse("D:/temp/logs/MiguApi__2018-06-14.log","d:/176.csv");
    analyse("D:/temp/logs/176_20180618.log","D:/temp/176_20180618.csv");
    analyse("D:/temp/logs/177_20180618.log","D:/temp/177_20180618.csv");