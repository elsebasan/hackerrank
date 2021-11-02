#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

    
def flippingBits(n):
    # Write your code here
    binario = format(n,"b")
    complement = ''
    lenght = len(binario)
    for i in range(32-lenght):
        binario = '0' + binario  
    for elem in binario:
        if elem == '1':
            complement = complement + '0'
        else:
            complement = complement + '1'
    return int(complement,2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
