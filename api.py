#!/usr/bin/env python
# encoding: utf-8

import os
from flask import Flask
from flask import request
import json


def send(to, content):
	cmd = 'gammu-smsd-inject -c /etc/gammu-smsdrc TEXT {} -unicode -text "{}"'.format(to, content)
	os.system(cmd)


def sendCdma(to, content):
	os.system('gammu-smsd-inject -c /etc/gammu-smsdrc-cdma TEXT {} -unicode -text "{}"'.format(to, content))


app = Flask(__name__)


@app.route('/cdma', methods=['GET'])
def cdma():
	to = request.args.get('to', '')
	content = request.args.get('content', '')
	print(to)
	print(content)
	# sendCdma(to, content)
	return '{}:{}'.format(to, content)


# 设置访问URL：'/plus'，methods：允许哪种方式访问
@app.route('/unicom', methods=['POST'])
def unicom():
	data = json.loads(request.data.decode())
	to = data['to']
	content = data['content']
	# send(to, content)
	print(to)
	print(content)
	return json.dumps(to + content)


if __name__ == '__main__':
	# 设置host，端口8080。threaded=True 代表开启多线程
	app.run(host='0.0.0.0', port=8080, threaded=True)
