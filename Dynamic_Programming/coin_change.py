# -*- coding: utf-8 -*-
"""
@author: Pulkit Maloo
@studentID: maloop

Bottom up approach is used to solve the problem as the bottom up approach avoids
the stack overflow problem.
Counts for base cases (n was less than 5) were calculated manually
{1:1(1), 2:1(11), 3:2(111,3), 4:4(1111,31,13,4)}
val is the DP table which stores the number of different partitions for ith number at index i

For i >= 5
If we select 1, then the number of partitions for remaining number will be val[i-1]
Similarly, if we selct 3, then the number of partitions for remaining number will be val[i-3]
Similarly, if we select 4, then the number of partitions for remaining number will be val[i-4]
Hence, total partitions for number i will be val[i-1] + val[i-3] + val[i-4]
"""

def partitions(n):
    val = [0, 1, 1, 2, 4]
    for i in xrange(5, n+1):
        val.append(val[i-1] + val[i-3] + val[i-4])
    return val[n]

numbers = [104029, 127708, 155281, 173736, 196047]
for n in numbers:
    print partitions(n)%(100000)