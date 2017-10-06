# -*- coding: utf-8 -*-
"""
@author: Pulkit Maloo
@studentID: maloop

Bottom up approach is used to solve the problem
jobs_list is a list of instances of the class Job
Initially jobs_list is sorted by finish time in ascending order
val is the DP table which stores maximum weight when i jobs are considered at index i
Base case is when there is only 1 job so only it will be considered
We consider jobs one by one from the jobs_list and analyze if including or
excluding it will maximize the weight
If we exclude it then weight would be (val[i-1])
If we include it then weight would be (weight + val[j]), where j is the index of
latest non-conflicting job before i
"""

class Job(object):
    def __init__(self, start, finish, weight):
        self.start = start
        self.finish = finish
        self.weight = weight

    def __lt__(self, other):
         return self.finish < other.finish

jobs_list = []
with open('input1.txt') as f:
    for job in f:
        j = map(int, job.split())
        jobs_list.append(Job(j[0], j[1], j[2]))
jobs_list.sort()

#def print_jobs(jobs_list=jobs_list):
#    for i in jobs_list:
#        print i.start, i.finish, i.weight

# Bottom Up
def max_weight(n=len(jobs_list), jobs_list=jobs_list):
    val = [0, jobs_list[0].weight]
    for i in xrange(2, n+1):
        inclusive_weight = jobs_list[i-1].weight
        for j in xrange(i-1, 0, -1):
            if jobs_list[j-1].finish <= jobs_list[i-1].start:
                inclusive_weight += val[j]
                break
        val.append(max(inclusive_weight, val[i-1]))
    return val[n]

print max_weight()