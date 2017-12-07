#!/usr/bin/python
# -*- coding: utf-8 -*-

from bitcoin import Btc
from bitcoin import Usdt
from stock import Hzsy

def test_get_usdt_price():
    f = open('usdt.html','rb')
    t = str(f.read())
    u = Usdt()
    assert(6.81 == u._extract_value(t))

def test_get_btc_price():
    f = open('usdt.html','rb')
    t = str(f.read())
    b = Btc()
    assert(73009.79 == b._extract_value(t))

def test_get_stock_price():
    f = open('hexun.json','rb')
    t = str(f.read())
    s = Hzsy()
    assert(50.3 == s._extract_value(t))
