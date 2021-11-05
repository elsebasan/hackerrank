#!/usr/bin/env python3
import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    aux = {1:0, 
           2:0,
           3:0,
           4:0,
           5:0
           }
    for elem in arr:
        aux[elem] = aux[elem] + 1
    count = 0
    result = 1
    for i in range(1,6):
        if aux[i] > count:
            count = aux[i]
            result = i
    return result
        
    
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

