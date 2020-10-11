#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:55:06 2020

@author: nm
"""

# Exception handling
try:
    print(5/ 0)
except Exception as e:
    print(e)
    pass

# Sentence generation 
subject = ['Americans', 'Indians']
verb = ['play', 'watch']
obj = ['Baseball', 'Cricket']

for x in subject:
    for y in verb:
        for z in obj:
            print(x, y, z)