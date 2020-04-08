#Problem Statment: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    Dictionary={}

    for i in range(len(note)):
        if note[i] not in Dictionary:
            Dictionary[note[i]]=0
        Dictionary[note[i]]+=1    
        
    for j in range(len(magazine)):
        if magazine[j] in Dictionary:
            Dictionary[magazine[j]]-=1
        else:
            continue    
        
        if Dictionary[magazine[j]]==0:
            del Dictionary[magazine[j]] 
    
        
    if len(Dictionary)==0:
        
        print "Yes"
    else:

        print "No"


if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
