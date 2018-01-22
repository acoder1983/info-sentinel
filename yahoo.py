#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from base import *


class Sbgx103(Target):

    def __init__(self):
        Target.__init__(self, 'sbgx103', "https://auctions.yahoo.co.jp/search/search?auccat=&p=sbgx103&tab_ex=commerce&ei=UTF-8&fr=", 
            300, Trigger([[">", 0]]))

    def _extract_value(self, text):
        m = re.compile('class="total".+class="count"')
        if m.search(text):
            total_count = m.search(text).group(0)
            m=re.compile('<em>\d+</em>')
            if m.search(total_count):
                return int(m.search(total_count).group(0)[4:-5])
        else:
            return 0


Yahoos = [
    Sbgx103(),
]
