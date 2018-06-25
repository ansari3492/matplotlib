# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:05:06 2018

@author: Lenovo
"""

import pandas as pd

import matplotlib.pyplot as plt
df=pd.read_csv("Automobile.csv")
make= pd.read_csv("Automobile.csv")
values_count=df.make.value_counts()



values=values_count.values
labels=values_count.index

plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.title("pie chart")
plt.show()