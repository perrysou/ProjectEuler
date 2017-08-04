import datetime
import time
from matplotlib.dates import date2num
import os
import glob
from scipy import io as spio

DIRFILENAME = '/Users/yangsu/Dropbox/research/'
FILENAME = 'xcorr_2013_342_PRN23_0343UT_zoom1_60s.mat'
OUTDIR = os.path.join(DIRFILENAME, FILENAME)
print OUTDIR

data = spio.loadmat(OUTDIR, matlab_compatible=True)
ESTV = data['ESTV']
ESTV.shape
