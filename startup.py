#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from datetime import datetime
from usdt import UsdtTarget

def main():
    targets = [UsdtTarget()]
    target = targets[0]
    while True:
        target.update()
        print('%s update target'%datetime.now())
        time.sleep(target.interval)


if __name__ == '__main__':
    main()
