# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:19:35 2020

@author: Gabriel Gelpi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data   = pd.read_csv('time_series_2019-ncov-Confirmed.csv')
data_d = pd.read_csv('time_series_2019-ncov-Deaths.csv')
data_re = pd.read_csv('time_series_2019-ncov-Recovered.csv')

data_col = data.columns.drop(['Province/State', 'Country/Region', 
                              'Lat', 'Long'])

paises = data[['Country/Region']].values.tolist()



def i_pais(paises,pais):
    for j,i in enumerate(paises):
        
        if i == [pais]:
            pos = j
    return pos

pais1 = ['Argentina','Chile','Brazil','Uruguay','Singapore']
nro_pos = np.int32(np.zeros(len(pais1)))
j = 0
for i in pais1:
    print('pais:',i)    
    ii = i_pais(paises,i)
    print('indice:',ii)
    nro_pos[j]= ii
    j=j+1
    
    

data_filt_conf = data.drop(index=[0],columns=['Province/State',
                      'Country/Region','Lat','Long'])

data_n = data_filt_conf.values

data_filt_d = data_d.drop(index=[0],columns=['Province/State',
                      'Country/Region','Lat','Long'])

data_d = data_filt_d.values

data_filt_r = data_re.drop(index=[0],columns=['Province/State',
                      'Country/Region','Lat','Long'])

data_r = data_filt_r.values

#34--> Brasil

for i in np.arange(0,len(nro_pos)): 
    print(i)
    plt.plot(data_col,data_n[nro_pos[i]-1,:],label=pais1[i])
    plt.fill_between(data_col, 0, data_n[nro_pos[i]-1,:], alpha=0.5)
    
"""    
plt.plot(data_col,data_d[nro_pos[0],:])
plt.plot(data_col,data_r[nro_pos[1],:])
plt.plot(data_col,data_n[65,:])

plt.fill_between(data_col, 0, data_n[65,:], facecolor='green', alpha=0.5)
plt.fill_between(data_col, 0, data_n[65,:], facecolor='orange', alpha=0.5)
plt.fill_between(data_col, 0, data_n[65,:], facecolor='blue', alpha=0.5)
"""
plt.grid()
plt.legend()
plt.xticks(np.arange(0,len(data_col),6))
plt.gcf().autofmt_xdate()

