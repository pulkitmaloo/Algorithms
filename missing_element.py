# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:09:11 2017

@author: PulkitMaloo
"""
import random as rand



def missing_element(arr, l, h):
    print l, h
    if l == h:
        return arr[l]
    m = (l + h) / 2
    if arr[m] == m:
        return missing_element(arr, m+1, h)
    else:
        return missing_element(arr, l, m-1)

if __name__ == "__main__":
    n = 10
    arr = list(range(1,n+1))
    x = rand.randint(1,n+1)
    arr.remove(x)
    n -= 1
    print arr, x
    print missing_element(arr, 0, n-1)