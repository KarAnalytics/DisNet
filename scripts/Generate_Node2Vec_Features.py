# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:00:46 2020

@author: Jinhang Jiang
"""

## Loard packages
import networkx as nx
from node2vec import Node2Vec
import pandas as pd
import numpy as np

## Read the file and trasform it to a networkx matrix
df= pd.read_csv('Data/network_table.csv', index_col=0)
graph=nx.from_numpy_matrix(df)


node2vec = Node2Vec(graph, dimensions=20, walk_length=5, num_walks=200, workers=4)
model = node2vec.fit(window=10, min_count=1)


##save for later use
model.wv.save_word2vec_format('embedding')
