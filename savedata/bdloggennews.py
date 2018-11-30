#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import re
import json


class Kafka_producer():
    '''
    使用kafka的生产模块
    '''

    def __init__(self, kafkahost, kafkaport, kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers='{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort
        ))

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            producer.send(self.kafkatopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print e


class Kafka_consumer():
    '''
    使用Kafka—python的消费模块
    '''

    def __init__(self, kafkahost, kafkaport, kafkatopic, groupid):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.groupid = groupid
        self.consumer = KafkaConsumer(self.kafkatopic, group_id=self.groupid,
                                      bootstrap_servers='{kafka_host}:{kafka_port}'.format(
                                          kafka_host=self.kafkaHost,
                                          kafka_port=self.kafkaPort))

    def consume_data(self):
        try:
            for message in self.consumer:
                yield message
        except KeyboardInterrupt, e:
            print e


def main():
    '''
    测试consumer和producer
    :return:
    '''
    ##测试生产模块
    names = ["ip_address", "sys_time", "report_type", "visit_time", "visitor_type", "user_id", "account_name",
             "phone_number", "os", "browser", "mac_address", "app_version", "visit_url"]
    linedict = {"ip_address": "", "sys_time": "", "report_type": "", "visit_time": "",
                "visitor_type": "", "user_id": "", "account_name": "", "phone_number": "", "os": "", "browser": "",
                "mac_address": "", "app_version": "", "visit_url": ""}

    producer = Kafka_producer("10.125.145.131", 9092, "pc_play_log")
    # for id in range(10):
    #    params = '{abetst}:{null}---'+str(i)
    #    producer.sendjsondata(params)
    ##测试消费模块
    # 消费模块的返回格式为ConsumerRecord(topic=u'ranktest', partition=0, offset=202, timestamp=None,
    # \timestamp_type=None, key=None, value='"{abetst}:{null}---0"', checksum=-1868164195,
    # \serialized_key_size=-1, serialized_value_size=21)

    consumer = Kafka_consumer('10.125.145.131', 9092, "pc_play_log", 'test-consumer-group')
    message = consumer.consume_data()
    for i in message:
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
        line = i.value
        for name in names:
            if (re.search(r"^(.*)" + name + "(.*)$", line)):
                tmpindex = line.find(name + ":")
                if tmpindex != -1:
                    tmpindex = tmpindex + len(name) + 1
                    # print name," is ",line[tmpindex:]
                    linedict[name] = line[tmpindex:len(line) - 1].strip()
        print linedict
        producer.sendjsondata(linedict)

if __name__ == '__main__':
    main()
