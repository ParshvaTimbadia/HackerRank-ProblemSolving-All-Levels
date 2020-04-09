Problem Statement: https://www.hackerrank.com/challenges/arrays-ds/problem

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.

def reverseArray(a):
    
    start=0 
    end=len(a)-1

    while (start<= end):

        swap(a, start, end)
        start+=1
        end-=1

    return a

def swap(list, pos1, pos2):

    list[pos1], list[pos2]= list[pos2], list[pos1]

    return list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
