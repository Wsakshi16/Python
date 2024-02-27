# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:30:35 2023

@author: adity
"""


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d = pd.read_csv("c:/0-datasets/Seeds_data.csv")
d.describe()
#Initialize the scalar
scalar = StandardScaler()
df = scalar.fit_transform(d)
dataset = pd.DataFrame(df)
res = dataset.describe()
#here if you will check res, in variable environment them

