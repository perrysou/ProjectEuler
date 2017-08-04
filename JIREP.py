# coding: utf-8

# # JIREP Project 07/07/2016

# ## Data structure
# JIC-BC-E, E stands for Este (East)
# JIC-BC-O, O stands for Oueste (West)
# The two receivers are 50 m apart, the baseline perperndicular to the geomagnetic field line

# In[1]:

import pandas
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
from matplotlib.dates import *
from scipy import io as spio
import os

# In[2]:

rx = ['E', 'O']
ipath = '../../Desktop/JRO_RX/'
prefix = 'JIC-BC-'
opath = './'

# ## Listing of GISTM Specific Logs

#
# |Command|Description|
# |:-----:|:-----:|
# | ISMCALIBRATIONSTATUS  | Current status of TEC self-calibration procedure |
# | ISMDETOBS  | Detrended phase and amplitude measurements
# | ISMRAWOBS  | Raw phase and amplitude measurements
# | ISMRAWTEC  | 1 second TEC measurements
# |ISMREDOBS|60 second reduced phase and amplitude measurements
# |ISMREDTEC|60 second reduced TEC measurements

# Download JULIA wind measurements from madrgial website

# In[3]:

# run globalIsprint.py --verbose --url=http://jro-db.igp.gob.pe/madrigal --parms=YEAR,MONTH,DAY,HOUR,MIN,SEC,GDLATR,GDLONR,GDALT,SNL,VIPE1,DVIPE1,VIPN1,DVIPN1 --output="JULIA.txt" --user_fullname="Yang+Su" --user_email=ysu27@hawk.iit.edu --user_affiliation="IIT" --startDate="03/01/2016" --endDate="05/05/2016" --inst=840 --kindat=1961

# In[5]:

# filepath = "//Users/yangsu/Desktop/JRO_RX/E_psn2.txt"
# tic = time.time()
# data = pandas.read_csv(filepath,delim_whitespace=True,header=None)
# #                       ,parse_dates=[[0,1,2]],infer_datetime_format=True,skip_blank_lines=True)
# data = np.array(data)
# print time.time() - tic
# print data.shape

# In[ ]:

# tic = time.time()
# sec = np.array([datetime.timedelta(seconds=s) for s in data[:,3]])
# ymd = [datetime.datetime(int(y),int(m),int(d),0,0,0) for y,m,d in
#      zip(data[:,0],data[:,1],data[:,2])]
# print time.time() - tic

# In[7]:

# print type(sec + ymd)
# tdata = sec + ymd
# #data = np.delete(data,,1)
# #dnum = date2num(ymd + sec)

# In[8]:

# tic = time.time()
# dnum = date2num(ymd + sec)
# print time.time() - tic

# In[20]:

#spio.savemat('file.mat', {'a': a}) # savemat expects a dictionary
data = spio.loadmat('../../Desktop/JRO_RX/E_scn.mat', struct_as_record=True)
data = data['data']
tic = time.time()
mat2pyoffset = 366.
data[:, 0] = data[:, 0] - mat2pyoffset
print data[:, 0]

# In[50]:

t0 = date2num(datetime.datetime(2016, 3, 29, 0, 0, 0))
print t0
tf = date2num(datetime.datetime(2016, 3, 31, 0, 0, 0))
print tf
#matlab_datenum = data[:,0]
#python_datetime = datetime.fromordinal(int(matlab_datenum)) + timedelta(days=matlab_datenum%1) - timedelta(days = 366)
megadata = data[(data[:, 0] <= tf) & (data[:, 0] >= t0) & (data[:, 2] >= 30
                                                           ), :]
print time.time() - tic
print megadata.shape

# In[ ]:

print megadata[:, 1:].max(axis=0)
fig1 = plt.figure(figsize=(16, 16))
a = np.array([0., -1. / 32., 1., 1. / 32.])

for prn in np.arange(1, 3):
    # for prn in np.unique(megadata[:,-1]):
    a[1] += 1. / 32
    plt.axes(a)
    #     plt.text(0, 0.5, str(prn), ha='center', va='center', size=12, alpha=1)
    #     plt.subplot(8,4,prn)
    rxdata = megadata[(megadata[:, -1] == prn), :]
    #     print rxdata.shape
    s4_L1_max = rxdata[:, 3].max()
    s4_L2_max = rxdata[:, 5].max()
    #     print s4_L1_max,s4_L2_max
    #     plt.plot_date(rxdata[:,0],rxdata[:,3],'r.',ms=1,label='s4_L1')
    plt.scatter(
        rxdata[:, 0],
        rxdata[:, 3],
        c=rxdata[:, 3],
        marker='o',
        cmap=plt.cm.jet,
        vmax=0.5,
        vmin=0,
        edgecolors='none',
        label='s4_L1')
    #     plt.plot_date(rxdata[:,0],rxdata[:,5],'ko',ms=1,label='s4_L2')
    #     plt.scatter(rxdata[:,0],rxdata[:,5],c=rxdata[:,5],marker='s',cmap=plt.cm.jet,vmax=0.5,vmin=0,edgecolors='none',label='s4_L2')
    ax = plt.gca()
    ax.set_frame_on(False)
    if prn == megadata[:, -1].min():
        ax.xaxis.set_major_locator(DayLocator())
        ax.xaxis.set_minor_locator(HourLocator())
        ax.xaxis.set_major_formatter(DateFormatter('%m-%d'))
        ax.xaxis.set_ticks_position('bottom')
        ax.set_title(r'L1 S_4')
        plt.legend()
    else:
        ax.xaxis.set_major_locator(DayLocator())
        ax.xaxis.set_minor_locator(HourLocator())
        ax.xaxis.set_ticklabels(())
#         plt.xticks()
    ax.set_xlim([t0, tf])
    ax.set_ylim([0, 0.5])
    plt.grid(True, which='both')
plt.tight_layout
plt.show()
fig1.savefig('test.pdf', bbox_inches='tight')

# In[93]:

tic = time.time()
#juliadata = np.genfromtxt('//Users/yangsu/Dropbox/research/JULIA.txt')
juliadata = pandas.read_csv(
    '//Users/yangsu/Dropbox/research/JULIA.txt',
    engine='python',
    delim_whitespace=True,
    header=None)
#                      ,parse_dates=[[0,1,2]],infer_datetime_format=True,skip_blank_lines=True)
print time.time() - tic
juliadata = np.array(juliadata)
