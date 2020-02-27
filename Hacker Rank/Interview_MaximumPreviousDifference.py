#!/bin/python3

import math
import os
import random
import re
import sys
'''
4
7
1
2
5

'''

#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY qty as parameter.
#

def maxCont(qty):
    maxdiff = float("-inf")
    for x in range(len(qty) - 1):
        for y in range(1, len(qty) - x):
            maxdiff = max(maxdiff, qty[x] - qty[x + y])
    print(maxdiff)

def maxDifference(qty):
    qty.reverse()
    res = [[qty[0]]]                    # Create a list of list,

    for i in range(1, len(qty)):        # Starting from 2nd element
        if qty[i - 1] > qty[i]:         # If the previous element is higher,  --> if the it's going down in the
                                        # direction we want
            res[-1].append(qty[i])      # Append the current element to the last list in res

        else:
            res.append([qty[i]])        # Else, append the current element to rest

    for n in range(0, len(res)):
        if len(res[n])>1:
            maxCont(res[n])




    # mylist=[]
    #
    # for i in range(len(arr)):
    #     if arr[i]<arr[i+1]:






if __name__ == '__main__':

    qty_count = int(input().strip())

    qty = []

    for _ in range(qty_count):
        qty_item = int(input().strip())
        qty.append(qty_item)

    result = maxDifference(qty)

