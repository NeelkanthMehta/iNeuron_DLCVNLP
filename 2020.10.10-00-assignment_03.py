#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:13:59 2020

@author: nm
"""

import itertools
import numpy as np
from functools import reduce


def myreduce(func,iterable):
    '''
    Implementation of reduce function from scratch
    '''
    final_value = iterable[0]
    for i in range(1,len(iterable)):
        final_value = func(final_value,iterable[i])
    return final_value


def myfilter(func, iterable):
    '''
    Implements filter function from scratch
    '''
    return [element for element in iterable if func(element)]


if __name__ == '__main__':
    my_list = list(range(1,20))
    print('func 1: ', myreduce(func=lambda a, b: a*(b/7), iterable=my_list))
    print('func 2: ', myfilter(func=lambda a: a%2==0, iterable=my_list))
    
    # list comprehensions
    ## lists formation
    l1 = [[i*y for i in range(1,5)] for y in ['x','y','z']]
    l2 = [[i*y for i in ['x','y','z']] for y in range(1,5)]
    l3 = [[[i] for i in range(y,y+3)] for y in range(2,5)]
    l4 = [list(range(i,i+4)) for i in range(2,6)]
    l5 = [[(i,y) for i in range(1,4)] for y in range(1,4)]
    
    ## final answer
    print(list(itertools.chain(*l1)))
    print(list(itertools.chain(*l2)))
    print(list(itertools.chain(*l3)))
    print(l4)
    print(list(itertools.chain(*l5)))