# Problem Statement: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    #Try jumping to steps forward if she can jump, else jump one step back
    i=0
    steps=0
    while i in range(len(c)-1):

        if i+2 < len(c) and c[i+2]!=1 :
            i+=2
        else:
            i+=1
        steps+=1
    
    return steps    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
