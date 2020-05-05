# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:16:30 2020

@author: Jinhang Jiang
"""

import pandas as pd
import os
import numpy as np


print (os.getcwd())
os.chdir('D:/OneDrive/RA—Karthik/EHR-MIT/Data')
os.chdir('C:/Users/jinha/OneDrive/RA—Karthik/EHR-MIT/Data')
print (os.getcwd())

diag = pd.read_csv('pid_icd10.csv')



## create the matrix
diag.head(9)
matrix = pd.get_dummies(diag.set_index('pid')['icd10'].astype(str)).max(level=0).sort_index()


diag_matrix = np.asmatrix(matrix)
diag_matrix_transpose = diag_matrix.transpose()
final_matrix = diag_matrix_transpose.dot(diag_matrix)

network_table = pd.DataFrame(final_matrix)


## append index name
icd10 = list(diag.icd10.unique())
icd10.sort()

network_table.index = icd10
network_table.columns = icd10

matrix.to_csv('frequency_matrix.csv')
network_table.to_csv('network_table.csv')
