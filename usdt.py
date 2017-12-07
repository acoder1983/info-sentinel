#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from base import *


class Usdt(Target):

    def __init__(self):
        self.name = 'huobi-usdt'
        self.source = "https://otc.huobi.pro/trade/list.html?coin=2&type=1"
        self.interval = 300
        self.trigger = Trigger([("<", 6.8), (">", 7.2)])

    def _extract_value(self, text):
        beg = text.find('/USDT<')
        end = text.find('CNY', beg)
        m = re.compile('\d\.\d+')
        return float(m.search(text[beg:end]).group(0))
