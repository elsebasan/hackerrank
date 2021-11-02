#!/usr/bin/env python3

import os
import re
import sys


def camelCase(element):
    splitorCombine, methodVariableClass, stringElement = element.split(";")
    #Split
    if splitorCombine == "S":
        # Method
        if methodVariableClass == "M":
            cap = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', stringElement[:-2])
            ans = " ".join(m.group(0).lower() for m in cap)
            return (ans.rstrip())
        #Variable
        if methodVariableClass == "V":
            cap = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', stringElement)
            ans = " ".join(m.group(0).lower() for m in cap)
            return (ans.rstrip())
        #Class
        if methodVariableClass == "C":
            cap = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', stringElement)
            ans = " ".join(i.lower() for i in cap)
            return (ans.rstrip())
    #Combine
    if splitorCombine == "C":
        # Method
        if methodVariableClass == "M":
            lst = stringElement.split(" ")
            res = []
            for i in range(len(lst)):
                if i == 0:
                    res.append(lst[i].lower())
                else:
                    res.append(lst[i].capitalize())
            ans = "".join(i for i in res)
            ans = ans.rstrip() + "()"
            return (ans.rstrip())
        #Variable
        if methodVariableClass == "V":
            lst = stringElement.split(" ")
            res = []
            for i in range(len(lst)):
                if i == 0:
                    res.append(lst[i].lower())
                else:
                    res.append(lst[i].capitalize())
            ans = "".join(i for i in res)
            return (ans.rstrip())
        #Class
        if methodVariableClass == "C":
            lst = stringElement.split(" ")
            ans = "".join(i.capitalize() for i in lst)
            return (ans.rstrip())


if __name__ == '__main__':
    while(True): 
        try:
            element = input().rstrip()
            result = camelCase(element)
            print (result)

        except EOFError:
            break







    
