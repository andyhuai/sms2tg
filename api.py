#!/usr/bin/env python
# encoding: utf-8

import os
from flask import Flask
from flask import request
import json


def send(to, content):
	cmd = 'gammu-smsd-inject -c /etc/gammu-smsdrc TEXT {} -unicode -text "{}"'.format(to, content)
	os.system(cmd)


def sendCdma():
	os.system('gammu-smsd-inject -c /etc/gammu-smsdrc-cdma TEXT 17607135876 -unicode -text "test----中文-电信"')


app = Flask(__name__)


@app.route('/cdma', methods=['GET'])
def hello_world():
	send('17607135876', '测试API')
	return 'Hello World!'


# 设置访问URL：'/plus'，methods：允许哪种方式访问
@app.route('/unicom', methods=['POST'])
def plus():
	data = json.loads(request.data.decode())
	to = data['to']
	content = data['content']
	send(to, content)
	return json.dumps(to + content)


if __name__ == '__main__':
	# 设置host，端口8080。threaded=True 代表开启多线程
	app.run(host='0.0.0.0', port=8080, threaded=True)
