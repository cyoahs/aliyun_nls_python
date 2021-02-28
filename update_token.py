# -*- coding: utf8 -*-
import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json

with open(os.path.join('config', 'accesskeyid'), 'r') as f:
    key_id = f.read()

with open(os.path.join('config', 'accesskeysecret'), 'r') as f:
    key_secret = f.read()

# 创建AcsClient实例
client = AcsClient(
   key_id,
   key_secret,
   "cn-shanghai"
);

# 创建request，并设置参数。
request = CommonRequest()
request.set_method('POST')
request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
request.set_version('2019-02-28')
request.set_action_name('CreateToken')
response = client.do_action_with_exception(request)
js = json.loads(response)

with open(os.path.join('config', 'token'), 'w') as f:
    f.write(js['Token']['Id'])

print(response)