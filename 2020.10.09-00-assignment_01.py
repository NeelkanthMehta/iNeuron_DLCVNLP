#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:32:41 2020

@author: nm
"""

import numpy as np

def assignment_01():
    '''
    A program which finds all such numbers between [2000 and 3200]
    that are divisible by 7 but are not multiple of 5
    and returns in a list
    '''
    mul7 = []
    for i in range(2000,3201):
        if (i % 7 == 0) and (i % 35 != 0):
            mul7.append(i)
    return mul7

def assignment_02():
    '''
    Enter your first name and last name, as prompted. You will get 
    your last name and first name printed with space between them.
    '''
    first_name = input('Your first name: ')
    last_name = input('Your last name: ')
    
    first_name, last_name = first_name.title(), last_name.title()
    print(last_name + ' ' + first_name)

def assignment_03():
    '''
    computes volume of a spear
    '''
    r = input("enter a radius value: ")
    try:
        r = float(r)
        assert r > 0, "radius cannot be 0 or less!"
        return round(4/3 * np.pi * r**3, 2)
    except Exception as e:
        print(e)


if __name__=='__main__':
    print(assignment_01())
    print('='*20)
    assignment_02()
    print('='*20)
    print(assignment_03())
