#!/usr/bin/env python3

import math
import os
import random
import re
import sys




#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    position = 0
    valleys = 0
    for direction in path:
        if direction == 'U':
            position = position + 1
        else:
            position = position - 1

        if position == 0 and direction == 'U':
            valleys = valleys + 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

