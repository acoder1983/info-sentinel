#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from datetime import datetime
from random import random

from bitcoin import BitCoins
from stock import Stocks


def main():
    targets = Stocks + BitCoins
    while True:
        for t in targets:
            try:
                t.update()
                print('%s update target' % datetime.now())
            except Exception as e:
                print(e)
            time.sleep(random())
        time.sleep(300)


if __name__ == '__main__':
    main()
