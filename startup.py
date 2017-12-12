#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from datetime import datetime
from random import random

from bitcoin import BitCoins
from stock import Stocks
import multiprocessing
import sys


def main(args):
    if len(args) > 1:
        run_as_daemon()
    else:
        run()


INTERVAL = 300


def run():
    targets = BitCoins + Stocks
    while True:
        with open('pid', 'w') as f:
            f.write(str(datetime.now()))
        for t in targets:
            try:
                t.update()
            except Exception as e:
                print(e)
            time.sleep(random())
        time.sleep(INTERVAL)


def run_as_daemon():
    p = None
    with open('pid', 'w') as f:
        text = 'init'
        f.write(text)
    while True:
        with open('pid') as f:
            t = f.read()
        if t != text:
            text = t
        else:
            if p is not None:
                print('%s terminating daemon' % datetime.now())
                p.terminate()
            p = multiprocessing.Process(target=run)
            p.start()
        time.sleep(INTERVAL * 3)


if __name__ == '__main__':
    main(sys.argv)
