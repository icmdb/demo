#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

import urllib
import urllib2

import json

AppKey = os.getenv("APP_KEY", "default_develop_key")
AppSecret = os.getenv("APP_SECRET", "default_develop_secret")
appcode = os.getenv("APP_CODE", "default_develop_code")


host = 'http://ali-hotword.showapi.com'
path = '/wordList'
method = 'GET'
#appcode = '你自己的AppCode'
querys = 'typeId=1'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()

if content:
    #print content
    res = json.loads(content)['showapi_res_body']['list']
    for item in res:
        #print res
        print item['num'],item['level'],item['trend'],item['name']

