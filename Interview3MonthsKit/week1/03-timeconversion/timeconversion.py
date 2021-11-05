#!/usr/bin/env python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#format recives '12:01:00PM'
def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    elif s[:2] == "12":
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:8] 
          







if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')




