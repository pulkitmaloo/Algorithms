#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 02:39:00 2017

@author: PulkitMaloo
"""

from collections import Counter


def get_frequency(filename='test.txt'):
    with open(filename, 'r') as f:
        data = f.read().decode("utf-8-sig").strip().lower()
#        data = f.read().strip().lower()
    freq = Counter(data)
    return dict(freq)


class Node(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __str__(self):
        return str(self.char) + ", " + str(self.freq)

    def __repr__(self):
        return "Node(" + str(self.char) + ", " + str(self.freq) + ')'


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return int((i - 1) / 2)


def min_heapify(arr, n, i):
    l = left(i)
    r = right(i)
    smallest = i
    if l < n and arr[l] < arr[i]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def build_minheap(arr, n):
    for i in range(int((n - 1) / 2), -1, -1):
        min_heapify(arr, n, i)


def contruct_heap(freq):
    nodes = []
    for ch in freq:
        nodes.append(Node(ch, freq[ch]))
    build_minheap(nodes, len(nodes))
    return nodes


def extract_min(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    m = arr[-1]
    del arr[-1]
    min_heapify(arr, len(arr), 0)
    return m


def insert(arr, x):
    arr.append(x)
    i = parent(len(arr) - 1)
    x_index = len(arr) - 1
    while i > 0 and arr[x_index] < arr[i]:
        arr[x_index], arr[i] = arr[i], arr[x_index]
        x_index = i
        i = parent(i)


def huffman(freq):
    Q, n = contruct_heap(freq), len(freq)
    for i in range(1, n):
        x = extract_min(Q)
        y = extract_min(Q)
        z = Node(x.char + y.char, x.freq + y.freq)
        z.left = x
        z.right = y
        insert(Q, z)
    return extract_min(Q)


def assign_code(x, code_so_far):
#    print x, "code", code_so_far
    if len(x.char) == 1:
        codes[x.char] = code_so_far
    else:
        assign_code(x.left, code_so_far + '0')
        assign_code(x.right, code_so_far + '1')

def size_saved(freq, codes):
    new_size = 0
    original = 0
    for key, val in codes.items():
        new_size += freq[key] * len(val)
        original += freq[key] * 8
    return original / (8 * 1024), new_size / (8 * 1024)

if __name__ == '__main__':
    filename = 'the_republic.txt'
    freq = get_frequency(filename)
    h = huffman(freq)
    codes = {}
    assign_code(h, '')
    org, new = size_saved(freq, codes)
    print org, "kb ->", new, "kb"
    print "Size saved:", org - new, "kb"



