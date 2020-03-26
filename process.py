#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:12:49 2020

From a Kaggle telecom churn dataset here:
    https://www.kaggle.com/becksddf/churn-in-telecoms-dataset

@author: david
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('~/telecom_churn/churn_vs_minutes.csv')
print(df['total_day_minutes'])

sns.set()
%matplotlib inline

sns.swarmplot(x='churn', y='total_day_minutes', data=df)

