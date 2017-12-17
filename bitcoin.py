#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from base import *


class Btc(Target):

    def __init__(self):
        Target.__init__(self, 'huobi-btc', "https://otc.huobi.pro/trade/list.html?coin=2&type=1", 300, Trigger([["<", 90000], [">", 120000]]))

    def _extract_value(self, text):
        m = re.compile('\d+\.\d{2}')
        val_t = m.search(text).group(0)[1:]
        return float(val_t)


class Usdt(Target):

    def __init__(self):
        Target.__init__(self,'huobi-usdt',"https://otc.huobi.pro/trade/list.html?coin=2&type=1",300,Trigger([["<", 6.85],[">", 7.25]]))

    def _extract_value(self, text):
        beg = text.find('/USDT<')
        end = text.find('CNY', beg)
        m = re.compile('\d\.\d+')
        return float(m.search(text[beg:end]).group(0))


BitCoins = [
    Btc(),
    Usdt()
]
