# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 03:02:57 2017

@author: PulkitMaloo
"""
def palindrome_partition(s):
    n = len(s)
    val = [[None]*n for i in range(n)]

    return val[0][n-1]