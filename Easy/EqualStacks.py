***
Problem Statement- https://www.hackerrank.com/challenges/equal-stacks/problem
***



#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    l1, l2, l3 = 0, 0, 0
    for each in h1:
        l1 = l1 + each
    for each in h2:
        l2 = l2 + each
    for each in h3:
        l3 = l3 + each
    while True:
        if l1==l2 and l2==l3:
            return l1
        if l1==0 and l2==0 and l3==0:
            return 0

        if max(l1, l2, l3) == l1:
            l1 = l1 - h1[0]
            h1.pop(0)
        elif max(l1, l2, l3) == l2:
            l2 = l2 - h2[0]
            h2.pop(0)
        else:
            l3 = l3 - h3[0]
            h3.pop(0)
   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')
