#Problem Statement: https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues



import math
import os
import random
import re
import sys

def isBalanced(s):
   
    stack = []

   
    for char in s:
        
        if char == '{' or char == '(' or char == '[':
            stack.append(char) # push
        
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return "NO"
            top_element = stack.pop() # pop
        
            if not Compare(top_element, char):
                return "NO"
      
    if len(stack) != 0:
        return "NO"
              
    return "YES"


# equal or not. 
def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True  
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
