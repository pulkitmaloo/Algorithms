# -*- coding: utf-8 -*-
def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2

def max_heapify(arr, n, i):
    l = left(i)
    r = right(i)
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_heap(arr, n):
    for i in range(n/2-1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr, n):
    build_heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

import random as rand
arr = [rand.randint(0, 100) for i in range(20)]
print arr

heap_sort(arr, len(arr))
print arr