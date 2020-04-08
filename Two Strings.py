#Problem Statement:https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


#!/bin/python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    Check={}
    for i in range(len(s1)):
        
        if s1[i] not in Check:
            Check[s1[i]]=1
        
      
    for j in range(len(s2)):
        if s2[j] in Check:
            return "YES"

    return"NO"        




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
