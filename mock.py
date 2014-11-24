# coding:utf-8

import hashlib
import urllib
import urllib2
import json

def _create_signature(message_arr):
    message_arr.sort()
    join_str = ''.join(message_arr)
    return hashlib.sha1(join_str).hexdigest()


timestamp = '1416794721093'
nonce = '213674821'
echostr = 'vIuz5ekD'
appsecret = 'appsecretEnF5leY4V'
signature = _create_signature([appsecret, timestamp, nonce])

# GET
url = 'http://127.0.0.1:8888/weibo/'
querys = {
    'signature': signature,
    'nonce': nonce,
    'echostr': echostr,
    'timestamp': timestamp
}
req = urllib2.Request(url + '?' + urllib.urlencode(querys))
request = urllib2.urlopen(req)
print request.read()

# POST
data = {
    "type": "text",
    "receiver_id": '1902538057',
    "sender_id": '2489518277',
    "created_at": "Mon Jul 16 18:09:20 +0800 2012",
    "text": "私信或留言内容",
    "data": {}
}

request = urllib2.urlopen(req, json.dumps(data))
print request.read()