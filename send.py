#!/usr/bin/env python
# encoding: utf-8
import time
import os


def send():
    os.system("sudo gammu-smsd-inject -c /var/gammu-smsdrc-cdma TEXT 17607135876 -text '测试一下'")


if __name__ == '__main__':
    send()