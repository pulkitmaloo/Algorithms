# -*- coding: utf-8 -*-

def edit_distance(s1, s2, m, n):
    val = [[0]*(n+1) for i in range(m+1)]
    for i in range(m):
        val[0][i] = n
    for i in range(n):
        val[i][0] = m
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                val[i][j] = val[i-1][j-1]
            else:
                val[i][j] = 1 + min(val[i][j-1],    # Insert
                                   val[i-1][j],     # Remove
                                   val[i-1][j-1])   # Replace
    return val[m][n]

s1 = "pulkit"
s2 = "maloo"

print(edit_distance(s1, s2, len(s1), len(s2)))