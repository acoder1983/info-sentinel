#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from base import *


class Btc(Target):

    def __init__(self):
        self.name = 'huobi-btc'
        self.source = "https://otc.huobi.pro/trade/list.html?coin=2&type=1"
        self.interval = 300
        self.trigger = Trigger([("<", 90000), (">", 110000)])

    def _extract_value(self, text):
        m = re.compile('\d{5}.\d{2}')
        return float(m.search(text).group(0))
