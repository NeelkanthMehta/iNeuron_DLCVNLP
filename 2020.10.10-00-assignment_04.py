#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:39:10 2020

@author: nm
"""

import numpy as np

class Triangle(object):
    
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def area(self):
        '''
        Computes area of a triangle
        '''
        s = self.perimeter()/ 2
        if s <= self.side1 or s <= self.side2 or s < self.side3:
            raise ValueError('One of your sides are less than the semiperimeter, select another value or another approach')
        a = np.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)).astype(np.float32)
        return round(a, 2)
    
    def perimeter(self):
        '''
        Computes perimeter of a triangle
        '''
        return (self.side1 + self.side2 + self.side3)


def filter_long_words(n,*args):
    '''
    Filters list of words from a given list that are of less than or equal to length n characters.
    '''
    return [i for item in args for i in item.split() if len(i)>n]

def count_words(*args):
    '''
    Counts number of times each word is repeated in the text.
    '''
    from collections import Counter
    return Counter([i for item in args for i in item.split()])


def vovel_detecter(word):
    '''
    '''
    vovels = ['a','e','i','o','u']
    for i in word:
        if i in vovels:
            print(i, True)
        else:
            print(i, False)


if __name__ == '__main__':
    triangle = Triangle(15,7,12)
    triangle.area()
    filter_long_words(3, "The violin string is first drawn on one side")
    count_words("The violin string is a first drawn on one of a sides")
    vovel_detecter("violin")
    