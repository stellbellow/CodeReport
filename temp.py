# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:13:12 2025

@author: Student Lab
"""

import numpy as np
import time
import pandas as pd
from os.path import exists
import sys
sys.path.append(r'C:\Users\Student Lab\Downloads\LabJackPython-2.1.0\LabJackPython-2.1.0\src')
import u6
import matplotlib.pyplot as plt
q=0

# =============================================================================
for i in range(0,99):
    q+=1
    variable=u6.U6()
    variable.configU6()
    voltage=variable.getAIN(0)

    tstart=time.perf_counter()
    datastorage=[]
    voltagestorage=[]
    freqhold=[]

    
    while time.perf_counter()-tstart<1:
        datastorage.append(time.perf_counter()-tstart)
        voltagestorage.append(variable.getAIN(0))
    datastorage=np.array(datastorage)
    voltagestorage=np.array(voltagestorage)
    
    tdiff=[]
    n=len(datastorage)
    for i in range (n-1):
        tdiff=datastorage[i+1]-datastorage[i]
    tdiff=np.array(tdiff)
    
    avg=np.mean(datastorage)
    avggap=np.mean(tdiff)
    voltavg=np.mean(voltagestorage)
    var=np.var(datastorage)
    std=np.std(tdiff)
# =============================================================================
#     var=np.var(datastorage)
#     std=np.std(datastorage)#np.std to find the standard deviation
# =============================================================================
    
    dic={'run': q,
         'mean':avggap,
         'timestd':std,
         'dark': -0.002265359426732673,
         'voltavg':voltavg
         'Frequency':[calcfreq]}
    print(dic)
    
# =============================================================================
#     xvals=datastorage
#     yvals=voltagestorage
#     plt.plot(xvals, yvals, label='Voltage vs. Time')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
# =============================================================================
# =============================================================================
#     xvals=np.linspace(0,50,num=250)
#     yvals=np.linspace(0,10, num=250)
# =============================================================================
    n=len(voltagestorage)
    X=np.fft.fft(voltagestorage)
    X_mag=((np.abs(X))**2)/n
    freq=np.fft.fftfreq(n,avggap)
    m=np.argmax(X_mag)
    calcfreq=np.abs(freq[m])
# =============================================================================
#     print(calcfreq)
# =============================================================================

# =============================================================================
# # =============================================================================
#     xvals=calcfreq
#     yvals=X_mag
# # =============================================================================
# 
# # =============================================================================
# 
# # =============================================================================
#     twodlst=[]
# 
#     def arr(n):
#         for i in range(n):
#             (x,y) = (X_mag[i], freq[i])
#             twodlst.append([x,y])
#         return(np.array(twodlst))
#     array=arr(n)
# 
# 
#     plt.plot(freq, X_mag, label='X Mag vs Frequency')
#     plt.xlabel('Frequency')
#     plt.ylabel('X Mag')
#     plt.xlim(right=300)
#     plt.xlim(left=0)
# =============================================================================
# =============================================================================
#     xvals=np.linspace(0,50,num=250)
#     yvals=np.linspace(0,10, num=250)
# =============================================================================
# =============================================================================
# =============================================================================
    #plt.show()
# =============================================================================
# =============================================================================
    
    dic={'Frequency':[calcfreq]}
    data=pd.DataFrame(dic)
    
    path=((r'C:\Users\Student Lab\Downloads\g1sampleexports.csv'))
    
    if exists(path):
        data.to_csv(path, mode='a',index=False,
                    header=False)
    else:
        data.to_csv(path, mode='w',index=False,
                    header=True)
        
        
        
d=pd.read_csv(path)
 
freqavg=np.mean(d['Frequency'])
freqstd=np.std(d['Frequency'])
print(freqavg)
print(freqstd)
