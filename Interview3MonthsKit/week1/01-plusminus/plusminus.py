#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positives = 0
    negatives = 0
    zeros  = 0
    lenght = len(arr)
    for elem in (arr):
        if elem < 0:
            negatives = negatives + 1
        elif elem == 0:
            zeros = zeros + 1
        else:
            positives = positives + 1

    print("{:.6f}".format(positives/lenght))
    print("{:.6f}".format(negatives/lenght))
    print("{:.6f}".format(zeros/lenght))




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

