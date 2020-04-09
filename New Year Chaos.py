# Problem Statement: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

***
This program was very good it really challenges your thinking process. I considered two options here. 

To work with only Number and it was just a trap for me as it passed all the tect cases mentioned in the prolem statement. However, I also had a backup plan and that was workin with both numbers and index. It is always wise to consider the second approach whenever you see a sorted sequence and a constant difference between indexes and number in the array. 

If you see such pattern you should try thinking in that particular direction. I have not seen any other solution yet but as far as this problem is concerned my solution is O(N).

Also, another interesting problem that you could use here is Bubble Sort but sorting with the help of it takes O(N*N). 
So Think Again.
***





#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    i=len(q)-1
    count=0
    while i> 0 :
        if q[i]!=i+1:

            if i-1 >= 0 and q[i-1]==i+1:
                count +=1
                swapPositions(q, i, i-1)


            
            elif i-2 >= 0 and q[i-2]==i+1:
                count +=2
                swapPositions(q, i-2, i-1)
                swapPositions(q, i-1, i)
            
            else:
                
                print "Too chaotic"
                return
        
        i-=1
    
    print count    

               
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
                


    

                


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
