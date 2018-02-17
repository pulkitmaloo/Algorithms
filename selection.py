# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:35:29 2017
@author: PulkitMaloo
"""
import random as rand

def partition(arr, low, high):
    pivot = rand.randint(low, high)
    arr[pivot], arr[high] = arr[high], arr[pivot]
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def selection(arr, low, high, i):
    """
    Finding ith smallest element in the arr
    low <= i <= high
    """
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if i == pivot_index:
        return arr[pivot_index]
    elif i < pivot_index:
        return selection(arr, low, pivot_index - 1, i)
    else:
        return selection(arr, pivot_index + 1, high, i)

x = 5
arr = [rand.randint(1, 100) for i in range(10)]
print selection(arr, 0, len(arr)-1, x)