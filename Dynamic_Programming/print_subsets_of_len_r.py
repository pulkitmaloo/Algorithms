# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:31:13 2017

@author: PulkitMaloo
"""
def printSubset(arr, data, n, r, index, i):
    if len(data) == r:
        print data
        return
    if i >= n:
        return
    # including the element
    include_data = data + [arr[i]]
    printSubset(arr, include_data, n, r, index+1, i+1)
    # excluding the element
    printSubset(arr, data, n, r, index, i+1)

s = list(range(1, 5))
n = len(s)
r = 2
printSubset(s, [], n, r, 0, 0)