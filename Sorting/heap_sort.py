# -*- coding: utf-8 -*-
def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2

def max_heapify(arr, n, i):
    l = left(i)
    r = right(i)
    largest = i
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)



arr = [3,4,2]

max_heapify(arr, len(arr), 0)