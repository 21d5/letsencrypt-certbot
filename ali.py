#!/usr/bin/python3
#coding=utf-8

import sys, tldextract, demjson 
# pip3 install aliyun-python-sdk-core-v3
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'default')
request = CommonRequest()

class AliDNS:
    def access_ali(self, action):
        request.set_accept_format('json')
        request.set_domain('alidns.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2015-01-09')
        request.set_action_name(action)

    # 增
    def add_domain_record(self, domainname, value, rr):
        self.access_ali('AddDomainRecord')
        request.add_query_param('DomainName', domainname)
        request.add_query_param('Type', 'txt')
        request.add_query_param('Value', value)
        request.add_query_param('RR', rr)

        response = client.do_action(request)
        return response

    # 删
    def delete_domain_record(self, recordid):
        self.access_ali('DeleteDomainRecord')
        request.add_query_param('RecordId', recordid)

        response = client.do_action(request)
        return response

    # 改
    def update_domain_record(self):
        self.access_ali('UpdateDomainRecord')
        request.add_query_param('RecordId', '1111')
        request.add_query_param('RR', '111')
        request.add_query_param('Type', '111')
        request.add_query_param('Value', '111')

        response = client.do_action(request)
        return response

    # 查
    def describe_domain_records(self, domainname):
        self.access_ali('DescribeDomainRecords')
        request.add_query_param('DomainName', domainname)

        response = client.do_action(request)
        return demjson.decode(response)
        #print(str(response, encoding = 'utf-8'))

file_name, certbot_domain, certbot_validation = sys.argv
#certbot_domain = CERTBOT_DOMAIN
#certbot_validation = CERTBOT_VALIDATION 
domain_arr = tldextract.extract(certbot_domain)
root_domain = domain_arr.registered_domain
rr = "_acme-challenge.%s" % domain_arr.subdomain

domain = AliDNS()
data = domain.describe_domain_records(root_domain)
record_list = data["DomainRecords"]["Record"]
if rr != '_acme-challenge.':
    if record_list:
        for item in record_list:
            if rr == item['RR']:
                domain.delete_domain_record(item['RecordId'])
else:
    rr = "_acme-challenge"

domain.add_domain_record(root_domain, certbot_validation, rr)
