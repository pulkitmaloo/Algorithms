# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 21:37:23 2017

@author: PulkitMaloo
"""

n = int(input())

fibonacci_numbers = [0, 1, 1]
fibonacci_numbers.extend([-1]*(n-2))

def fibonacci(n, fib=fibonacci_numbers):
    if n < 3:
        return 1
    elif fib[n] > 0:
        return fib[n]
    else:
        fib[n] = fibonacci(n-1, fib) + fibonacci(n-2, fib)
        return fib[n]

print fibonacci(n, fibonacci_numbers)