# Problem Statement:https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python
# Method 1: Using Python Function

***
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    x=0
    while d>0:
        x=a.pop(0)
        a.append(x)
        d-=1
    return a    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
***

# METHOD 2: Without Using Python Funtions with logic:

def rotLeft(a, d):
    
    RotedArr= []
    index=d
    i=0
    size=len(a)
    

    while index < size:
        
        RotedArr[i]=a[index]
        i+=1
        index+=1
        
    
    index=0
    while index < d:
        RotedArr[i]=a[index]
        i+=1
        index+=1
    
    return RotedArr
