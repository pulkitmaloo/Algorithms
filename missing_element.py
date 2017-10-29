# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:09:11 2017

@author: PulkitMaloo
"""
n = 10
a = list(range(1,n+1))
import random as rand
x = rand.randint(1,n+1)
a.remove(x)
print a