#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
from datetime import datetime

from pymongo import MongoClient

from mail import send_mail


class Trigger:
    def __init__(self, cond_values):
        self.cond_values = cond_values

    def triggered(self, cur_val):
        for cv in self.cond_values:
            if (cv[0] == "<" and cur_val <= cv[1]) or \
                    (cv[0] == ">" and cur_val >= cv[1]):
                return True
        return False


class Target:

    def __init__(self, name, source, interval, trigger):
        self.name = name
        self.source = source
        self.interval = interval
        self.trigger = trigger
        self.cur_val = 0.

    def update(self):
        new_val = self._get_from_source()
        if not self._is_val_valid(new_val):
            print('%s %s %s is invalid' % (datetime.now(), self.name, new_val))
            return
        client = MongoClient('mongodb://192.168.1.100:27017')
        db = client.sentinel
        db[self.name].insert_one({'timestamp': datetime.now(),
                                  'value': new_val})
        print('%s save %s %s' % (datetime.now(), self.name, new_val))

        if self.trigger.triggered(new_val) and new_val != self.cur_val:
            self.cur_val = new_val
            self._action(new_val)

    def _is_val_valid(self, val):
        return val > 0.

    def _get_from_source(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        r = urllib.request.Request(self.source, headers=headers)
        f = urllib.request.urlopen(r)
        t = str(f.read())
        return self._extract_value(t)

    def _extract_value(self, text):
        pass

    def _action(self, cur_val):
        send_mail('%s %s' % (self.name, cur_val), '')
