#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:48:15 2020

@author: nm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def moving_average(a, window=4):
    '''
    Returns moving average of a given array and window
    '''
    ret = np.cumsum(a, dtype=np.float16)
    ret[window:] = ret[window:] - ret[:-window]
    return ret[window-1:]/ window

def power(ser, power=1, increasing=False):
    '''
    Raises a pandas.Series() into a power
    '''
    df = ser.copy(deep=True)
    df = pd.DataFrame(df, columns=['original'])
    if power > 1:
        if increasing==False:
            df['power_'+str(power)] = ser.pow(power, fill_value=0)
        elif increasing==True:
            for i in range(2, power+1):
                df['power_'+str(i)] = ser.pow(i, fill_value=0)
    return df


if __name__ == '__main__':
    # power
    sample_series = pd.Series([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
    modified_sample = power(ser=sample_series, power=3)
    
    # Moving Average Fn
    moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150], window=3)
    
    # alternatively
    pd.Series([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]).rolling(window=3).mean()[2:].round(2)
