# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:16:30 2020

@author: Jinhang Jiang
"""

import pandas as pd
import os



print (os.getcwd())
os.chdir('D:/OneDrive/RA—Karthik/EHR-MIT/Data')
os.chdir('C:/Users/jinha/OneDrive/RA—Karthik/EHR-MIT/Data')
print (os.getcwd())




## create the matrix
diag = pd.read_csv('pid_icd10.csv')
diag.head(9)
matrix = pd.get_dummies(diag.set_index('pid')['icd10'].astype(str)).max(level=0).sort_index()




df = diag.head(100000)
df.head()
matrix = pd.get_dummies(df.set_index('pid')['icd10'].astype(str)).max(level=0).sort_index()

# check on binary
a=matrix.iloc[0]
a

