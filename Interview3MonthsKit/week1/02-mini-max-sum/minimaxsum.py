#!/usr/bin/env python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minimun = sum(arr) - max(arr)
    maximun = sum(arr) - min(arr)
    print(str(minimun)+' '+ str(maximun))
    


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

