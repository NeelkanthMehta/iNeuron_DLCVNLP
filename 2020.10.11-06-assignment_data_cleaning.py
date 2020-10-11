#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 07:41:22 2020

@author: nm
"""

import re
import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']
                   }
                  )

# Splitting Col 1 to 2 columns
def split_col_1(drop=False):
    Departure = []
    Destination = []
    for _, val in df['From_To'].iteritems():
        Departure.append(val.split('_')[0].lower()), Destination.append(val.split('_')[1].lower())
    
    if drop:
        df.drop(labels='From_To', axis=1, inplace=True)
    return Departure, Destination

# FillNaN FlightNumber
def fill_col_2():
    df['FlightNumber'] = np.where(df['FlightNumber'].isnull(), df['FlightNumber'].shift(1)+10, df['FlightNumber']).astype(np.int32)

# Transform RecentDelays to num of recent delays and average delay
def transform_col_3(drop=False):
    NumRecentDelays = []
    AverageDelayRte = []
    for _, val in df['RecentDelays'].iteritems():
        elements = len(val)
        NumRecentDelays.append(elements)
        
        total_delay = 0 if elements==0 else sum(val)
        if elements > 0:
            AverageDelayRte.append(total_delay/elements)
        else:
            AverageDelayRte.append(0)
    
    if drop:
        df.drop(labels=['RecentDelays'], inplace=True, axis=1)
    return NumRecentDelays, AverageDelayRte


# Cleaning Airline
def clean_col_4():
    airline = []
    for _, val in df['Airline'].iteritems():
        txt = re.findall('[a-zA-Z]+', val)
        txt = ' '.join([i for i in txt])
        airline.append(txt)
    return airline


if __name__ == '__main__':
    df['From'], df['To'] = split_col_1(drop=True)
    fill_col_2()
    df['NumRecentDelays'], df['AvgDelayMinutes'] = transform_col_3(drop=True)
    df['Airline'] = clean_col_4()
