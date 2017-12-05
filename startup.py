#!/usr/bin/python
# -*- coding: utf-8 -*-

from usdt import UsdtTarget

def main():
    targets = [UsdtTarget()]
    target = targets[0]
    while True:
        target.update()
        time.sleep(target.interval)


if __name__ == '__main__':
    main()
