#!/usr/bin/env python3
import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    dictionary = {}
    for elem in s:
        elem = elem.lower() 
        if elem.isalpha() and not (elem in dictionary):
            dictionary[elem] = elem
    if len(dictionary) == 26:
        return "pangram"
    else:
        return "not pangram"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

