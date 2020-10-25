#!/usr/bin/env python
# encoding: utf-8
import time
import os


def send():
    os.system('gammu-smsd-inject -c /etc/gammu-smsdrc-cdma TEXT 17607135876 -text "test----123"')


if __name__ == '__main__':
    send()