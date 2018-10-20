# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:47:09 2015

@author: victor
"""

#fonctions générales

import numpy as np
from random import random
import time

signe=lambda x:(np.abs(x)/x if x!=0 else 1)

alea = lambda a,b : a + (b-a)*random()

def getTime():
    T=time.localtime()
    s=str(T[0])
    for i in range(1,len(T)-5):
        s+="_"+str(T[i])
    s+="h"+str(T[-5])
    return s


