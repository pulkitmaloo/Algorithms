# -*- coding: utf-8 -*-
def longest_palindrome(s):
    """
    Returns the length of the longest palindromic subsequence in s in O(n^2)
    """
    n = len(s)
    val = [[0]*n for i in range(n)]
    for i in range(n):
        val[i][i] = 1
    for sl in range(2, n+1):
        for i in range(n-sl+1):
            j = i + sl - 1
            if s[i] == s[j]:
                if sl == 2:
                    val[i][j] = 2
                else:
                    val[i][j] = val[i+1][j-1] + 2
            else:
                val[i][j] = max(val[i+1][j], val[i][j-1])
    return val[0][n-1]

s = "geeks for geeks"
print longest_palindrome(s)