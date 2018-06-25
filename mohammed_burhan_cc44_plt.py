# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:56:11 2018

@author: Lenovo
"""

import pandas as pd


from sklearn.model_selection import train_test_split
df=pd.read_csv("Cars.csv")
X=df.iloc[:,:1].values

y=df.iloc[:,0].values
col_names=list(df.columns)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
data_x1=pd.DataFrame(X_train)
data_x1.to_csv("X_train.csv")
data_x2=pd.DataFrame(X_test)
data_x2.to_csv("X_test.csv")
data_y1=pd.DataFrame(y_train)
data_y1.to_csv("y_train.csv")
data_y2=pd.DataFrame(y_test)
data_y2.to_csv("y_test.csv")
