#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

from pymongo import MongoClient


class Trigger:
    def __init__(self, cond_values):
        self.cond_values = cond_values

    def triggered(self, cur_val):
        for cv in self.cond_values:
            if (cv[0] == "<=" and cur_val <= cv[1]) or \
                    (cv[0] == ">=" and cur_val >= cv[1]):
                return True
        return False


class Target:

    def __init__(self, name, source, interval, trigger):
        self.name = name
        self.source = source
        self.interval = interval
        self.trigger = trigger

    def update(self):
        cur_val = self._get_from_source()
        client = MongoClient('mongodb://192.168.1.100:27017')
        db = client.sentinel
        db[self.name].insert_one({'timestamp': datetime.now(),
                                  'value': cur_val})
        if self.trigger.triggered(cur_val):
            self._action(cur_val)

    def _get_from_source(self):
        pass

    def _action(self,cur_val):
        pass
