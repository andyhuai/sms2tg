#!/usr/bin/env python
# encoding: utf-8
import time
import gammu.smsd
import sys

receptNum = '+8617607135876' #自己的电话号码
smsd = gammu.smsd.SMSD('/etc/gammu-smsdrc')


def send_message(msg):
  message = {
     'Text': msg,
     'SMSC': {'Location': 1},
     'Number': receptNum,
     'Coding': 'Unicode_No_Compression'
   }
  #print(message)
  smsd.InjectSMS([message])

if __name__ == '__main__':
  send_message('测试一下')