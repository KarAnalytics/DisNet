# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:57:36 2020

@author: Jinhang Jiang
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string as str
import re as re
import getpass


#%matplotlib inline
print(os.getcwd())
os.chdir('C:/Users/jinha/OneDrive/RA—Karthik/EHR-MIT/Data')
print(os.getcwd())

diagnosis = pd.read_csv('diagnosis.csv')
diagnosis.shape
diagnosis.head()


unique_diagnosis = diagnosis.diagnosisstring.unique()
len(unique_diagnosis)

icd10 = pd.read_csv("icd10.csv")
len(icd10)
icd10.head

#icd10['trans_icd10'] = icd10.C1+ '.' +icd10.C2
icd10.trans_icd10.head()

#icd10.to_csv("icd10.csv", index = False)

#diagnosis['icd9'] = diagnosis['icd9code'].str.split("[A-Z]",expand=True)
#diagnosis['icd9'] = diagnosis['icd9code'].str.split(",",expand=True)
diagnosis.icd9.head()
diagnosis['icd9']

df = diagnosis['icd9code'].str.split(",",expand=True)
diagnosis['icd10']=df[1]
diagnosis['icd9'] =df[0]
diagnosis.icd10.head()




a=diagnosis.icd9.dropna().str.isupper()
###########################1488 1489
a.drop(a[a == False].index, inplace=True)
len(a) #36704
b=diagnosis.loc[a.index,]
len(b.icd9.unique()) #73
diagnosis.icd10.loc[a.index,]=diagnosis.icd9.loc[a.index,]
diagnosis.icd9.loc[a.index,]=np.nan



unique_icd9=diagnosis['icd9'].dropna().unique()
len(unique_icd9)  #919
len(diagnosis.icd9.dropna())



unique_icd10=diagnosis['icd10'].dropna().unique()
len(unique_icd10)
len(diagnosis.icd10.dropna())



#diagnosis.to_csv("diag.csv", index = False)




####icd10 transformation
icd10['trans_icd10']=icd10.trans_icd10.fillna(0)

for i in range(0,71704):
    print(i)
    if icd10.trans_icd10[i] == 0:
        icd10.trans_icd10[i] = icd10.C1[i]
