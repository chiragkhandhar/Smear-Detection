# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:40:29 2020

@author: Chirag
"""

def pipeThrough(*fns):
    def result_fn(datum):
        acc = datum
        for fn in list(fns):
            acc = fn(acc)
        return acc
    return result_fn

def last(lst):
    return lst[-1]
