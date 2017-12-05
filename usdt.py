#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib.request
from mail import send_mail

from base import *


class UsdtTarget(Target):

    def __init__(self):
        self.name = 'huobi-usdt'
        self.source = "https://otc.huobi.pro/trade/list.html?coin=2&type=1"
        self.interval = 300
        self.trigger = Trigger([("<=", 6.71)])

    def _get_from_source(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        r = urllib.request.Request(self.source, headers=headers)
        f = urllib.request.urlopen(r)
        t = str(f.read())
        beg = t.find('/USDT<')
        end = t.find('CNY', beg)
        m = re.compile('\d\.\d+')
        return float(m.search(t[beg:end]).group(0))

    def _action(self, cur_val):
        send_mail('usdt %s' % cur_val, '')
        print('usdt %s' % cur_val)
