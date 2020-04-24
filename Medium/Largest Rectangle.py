***
Problem Statement: https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues



***


#!/bin/python3
from collections import deque 
import math
import os
import random
import re
import sys

# Complete the largestRectangle functions below.
def largestRectangle(heights):
    
      stack = [-1]
      maxArea = 0

      for i in range(len(heights)):
          # we are saving indexes in stack that is why we comparing last element in stack
          # with current height to check if last element in stack not bigger then
          # current element
          while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                lastElementIndex = stack.pop()
                maxArea = max(maxArea, heights[lastElementIndex] * (i - stack[-1] - 1))
                

                
          stack.append(i)

      # we went through all elements of heights array
      # let's check if we have something left in stack
      while stack[-1] != -1:
          lastElementIndex = stack.pop()
          maxArea = max(maxArea, heights[lastElementIndex] * (len(heights) - stack[-1] - 1))

      return maxArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
