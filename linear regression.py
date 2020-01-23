# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:25:54 2020

@author: Dell
"""

import json
import matplotlib.pyplot as pyp
import numpy as np
def estimate_coef(x, y): 
    n = np.size(x) 
    m_x, m_y = np.mean(x), np.mean(y) 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x   
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    pyp.scatter(x, y, color = "r", marker = "o", s = 2) 
    y_pred = b[0] + b[1]*x 
    pyp.plot(x, y_pred, color = "g") 
    pyp.title('TEMPURATUTE')
    pyp.xlabel('Year') 
    pyp.ylabel('t') 
    pyp.show()
    
    
    
f = open('temp.json','r')
txt =f.read()
ob=json.loads(txt)
y=[]
temp=[]
avgstat=[]
for year in ob['data']:
    avg=0
    y.append(int(year[0]))
    for ad in year[1:]:
        
        avg+=float(ad)
    avgstat.append(avg/len(year[1:]))
    temp.extend(year[1:])
pyp.plot(y,avgstat)
pyp.axis([1900,2016,23,27])
pyp.show()
x = np.array(y) 
y = np.array(avgstat) 
b = estimate_coef(x, y) 
print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1])) 
plot_regression_line(x, y, b)
