# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:36:13 2018

@author: Lenovo
"""
import urllib.request
import matplotlib.pyplot as plt

wiki="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
page=urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
right_table=soup.find_all('table',class_="wikitable")
body_list=right_table[0].find_all("tr")

state_ter=[]
national_share=[]
for row in body_list[1:-1]:
    cells=row.find_all('td')
    state_ter.append((cells[1]).text.strip())
    national_share.append((cells[4]).text.strip())
    
    
import pandas as pd
df=pd.DataFrame()
df['State / Territory']=state_ter
df['National Share']=national_share
df[:6]
print(df)


#pie charts
#plt.rcdefaults()
values=list(national_share[0:6])
labels=list(state_ter[0:6])
explode=[0.3,0,0,0,0,0]
fig1, ax1 = plt.subplots()
plt.pie(values,labels=labels,autopct='%1.1f%%',explode=explode)
plt.title("pie chart")
plt.show()
        

   


