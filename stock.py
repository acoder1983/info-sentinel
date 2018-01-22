#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re

from base import *


class Stock(Target):

    def __init__(self, name, interval, trigger, stock_code):
        Target.__init__(self, name, '', interval, trigger)
        self.source = 'http://webstock.quote.hermes.hexun.com/a/quotelist?code=%s&column=code,price,priceweight' % stock_code

    def _extract_value(self, text):
        m = re.compile('\{.+\}')
        t = m.search(text).group(0).replace(
            ' ', '').replace('\\r', '').replace('\\n', '')
        r = json.loads(t)
        return int(r['Data'][0][0][1]) / int(r['Data'][0][0][2])


class Hzsy(Stock):
    def __init__(self):
        Stock.__init__(self, 'stock-hzsy', 300,
                       Trigger([["<", 7.0], [">", 8.5]]), 'SSE600191')


class Qsgf(Stock):
    def __init__(self):
        Stock.__init__(self, 'stock-qsgf', 300,
                       Trigger([["<", 4.5], [">", 5.3]]), 'SZSE002638')


class Zygf(Stock):
    def __init__(self):
        Stock.__init__(self, 'stock-zygf', 300,
                       Trigger([["<", 7.5], [">", 8.6]]), 'SSE600770')


class Jnjj(Stock):
    def __init__(self):
        Stock.__init__(self, 'stock-jnjj', 300,
                       Trigger([["<", 40]]), 'SSE601313')


class Shgf(Stock):
    def __init__(self):
        Stock.__init__(self, 'stock-shgf', 300,
                       Trigger([["<", 11.0], [">", 13.0]]), 'SZSE000014')


Stocks = [
# Hzsy(), 
Qsgf(), 
# Zygf(), Jnjj(), Shgf()
]
