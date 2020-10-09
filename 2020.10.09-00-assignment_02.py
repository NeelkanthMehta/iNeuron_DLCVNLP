#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:23:36 2020

@author: nm
"""

import numpy as np

def assignment_01():
    '''
    Pattern creation using nested loops
    '''
    values = [i for i in range(1,6)]
    for i in values[-2::-1]:
        values.append(i)
    for i in values:
        print('*'*i)

def assignment_02():
    '''
    Reverses the input from the user
    '''
    word = input('enter a word: ')
    print(word[::-1])


if __name__ == '__main__':
    assignment_01()
    assignment_02()
