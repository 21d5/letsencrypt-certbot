#!/bin/bash

# 阿里云操作 DNS Hook

PATH=$(cd `dirname $0`; pwd)

echo $PATH"/ali.py"

# 调用 Python 脚本，自动设置 DNS TXT 记录。
# 第一个参数：需要为那个域名设置 DNS 记录
# 第二个参数：letsencrypt 动态传递的 Value 值 

echo $CERTBOT_DOMAIN $CERTBOT_VALIDATION

$PATH"/ali.py"  $CERTBOT_DOMAIN $CERTBOT_VALIDATION >"/var/log/certdebug.log"

# DNS TXT 记录刷新时间
/bin/sleep 20

echo "END"
###
