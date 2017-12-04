#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import time
import urllib
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

TARGETS_INFO = [{
    "name": "huobi-c2c-usdt",
    "source": "https://otc.huobi.pro/trade/list.html?coin=2&type=1",
    "interval": 1,
    "trigger": {
        "cond": "<=",
        "value": 6.85
    }
}]


class Trigger:
    def __init__(self, cond, value):
        self.cond = cond
        self.value = value

    def update(self, cur_val):
        if self.cond == "<=" and cur_val <= self.value:
            pass


class Target:
    @staticmethod
    def load_targets():
        targets = []
        for ti in TARGETS_INFO:
            t = Target(ti['name'], ti['source'], ti['interval'],
                       Trigger(ti['trigger']['cond'], ti['trigger']['value']))
            targets.append(t)
        return targets

    def __init__(self, name, source, interval, trigger):
        self.name = name
        self.source = source
        self.interval = interval
        self.trigger = trigger

    def update(self):
        cur_val = self.getFromSource()
        client = MongoClient('mongodb://192.168.1.100:27017')
        db = client.sentinel
        db[self.name].insert_one({'timestamp': datetime.now(),
                                  'value': cur_val})
        self.trigger.update(cur_val)

    def getFromSource(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        r = urllib.request.Request(self.source, headers=headers)
        f = urllib.request.urlopen(r)
        t = str(f.read())
        beg = t.find('/USDT<')
        end = t.find('CNY', beg)
        m = re.compile('\d\.\d+')
        return float(m.search(t[beg:end]).group(0))


def main():
    targets = Target.load_targets()
    target = targets[0]
    while True:
        target.update()
        time.sleep(target.interval)


if __name__ == '__main__':
    main()
