#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:40:40 2018

@author: areed145
"""

import pandas as pd

#data = pd.read_csv("https://www.bgc-jena.mpg.de/wetter/mpi_roof_2016b.zip", sep="\,\s*", encoding='cp1252')
#
#cols = ['datetime', 'p', 'T', 'Tpot', 'Tdew', 'rh', 'VPmax', 'VPact',
#       'VPdef', 'sh', 'H2OC', 'rho', 'wv', 'max.wv', 'wd', 'rain',
#       'raining', 'SWDR', 'PAR', 'max.PAR', 'Tlog', 'CO2']
#
#data.columns = cols
#
#data.to_csv('data.csv', index=False)

data = pd.read_csv('data.csv')

data.index = pd.to_datetime(data.datetime)

data = data.drop('datetime', axis=1)

data.apply(pd.to_numeric)

data = data.resample('1H').interpolate(method='spline', order=2)

data_diff = data.diff()

data_diff.plot(y='p')
data_diff.plot(y='T')

data.plot(y='p')
data.plot(y='T')
