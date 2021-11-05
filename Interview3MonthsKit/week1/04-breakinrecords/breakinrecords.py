#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here         
    maximun = scores[0]
    minimun = scores[0]
    count_min = 0
    count_max = 0
    lenght = len(scores)
    for i in range(1,lenght):
        if scores[i] > maximun:
            maximun = scores[i]
            count_max = count_max + 1
        if scores[i] < minimun:
            minimun = scores[i]
            count_min = count_min + 1
    return [count_max,count_min]





if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))




