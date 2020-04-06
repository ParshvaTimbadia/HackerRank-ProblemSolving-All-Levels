# ProblemStatement- https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Here I attach the solution 


import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    Valley_Count=0
    Total_Sum=0

    for i in range(len(s)):

        if s[i]=='U':
            Total_Sum+=1
        else:
            Total_Sum-=1
        if Total_Sum==0 and s[i]=='U':
            Valley_Count+=1  
    
    return Valley_Count


    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
