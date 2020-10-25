#!/usr/bin/env python
# encoding: utf-8
import time
import os


def send():
    os.system('gammu-smsd-inject -c /etc/gammu-smsdrc TEXT 17607135876 -unicode -text "test----中文-联通"')


def sendCdma():
    os.system('gammu-smsd-inject -c /etc/gammu-smsdrc-cdma TEXT 17607135876 -unicode -text "test----中文-电信"')


if __name__ == '__main__':
    send()
    sendCdma()