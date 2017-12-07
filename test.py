#!/usr/bin/python
# -*- coding: utf-8 -*-

from btc import Btc
from usdt import Usdt

def test_get_usdt_value():
    f = open('usdt.html','rb')
    t = str(f.read())
    u = Usdt()
    assert(6.81 == u._extract_value(t))

def test_get_btc_value():
    f = open('usdt.html','rb')
    t = str(f.read())
    b = Btc()
    assert(73009.79 == b._extract_value(t))
