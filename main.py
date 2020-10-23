#!/usr/bin/env python3
import logging
import at
import json
import datetime
import sqlite3
import requests
import time

logging.basicConfig(level=logging.DEBUG)


def push2Bark(text):
    url = "https://api.day.app/DF4Dz7FwJXwJp92o7H4NzU/{}?isArchive=1"
    res = requests.get(url.format(text))
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(res.text)
    print('*************************')


def on_message(source: str, content: str, timestamp: datetime.datetime, pdu: str):
    logging.info('New message from {} at {}: {}'.format(
        source, timestamp.strftime('%c'), content))
    message = config['notification_format']['message'].format(source=source, timestamp=timestamp.strftime('%c'),
                                                              content=content, label=config['sms']['label'])
    push2Bark(message)
    dbc.execute('INSERT INTO sms(`from`, `to`, `content`, `timestamp`, `pdu`) VALUES(?, ?, ?, ?, ?)',
                (source, config['sms']['label'], content, timestamp, pdu))
    dbconn.commit()


def on_call(source: str):
    logging.info('Incoming call from {}'.format(source))
    message = config['notification_format']['call'].format(
        source=source, timestamp=datetime.datetime.now(), label=config['sms']['label'])
    logging.info(message)

# dbc.execute('INSERT INTO sms(`from`, `to`, `content`, `timestamp`, `pdu`) VALUES(?, ?, ?, ?, ?)',
#    (source, config['sms']['label'], content, timestamp, pdu))
# dbconn.commit()


outbox = dict()

if __name__ == '__main__':
    logging.info('Starting sms2tg')
    config = json.loads(open('config.json', 'r').read())

    dbconn = sqlite3.connect(config['db']['path'])
    dbc = dbconn.cursor()

    at.init(config['sms']['device_path'], config['sms']['device_baudrate'])
    at.set_callback(on_message, on_call)
    at.set_reply_audio(config['phone']['autoreply_with_audio'],
                       config['phone']['autoreply_audio_exec'])
    at.start()
