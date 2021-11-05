#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#



def marsExploration(s):
    # Write your code here
    count = 0
    module = 0
    for elem in s:
        if (module == 0 or module == 2 )and not (elem == "S"):
            count = count + 1
        elif module == 1 and not(elem == "O"):
            count = count + 1
        module = (module + 1 ) % 3
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

