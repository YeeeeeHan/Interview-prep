#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from Node import Node



#
# Complete the 'getMinimumUniqueSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def getMinimumUniqueSum(arr):
#     arr.sort()
#     for i in range(len(arr)):
#         x = i
#         while True:
#             if arr[i] == arr[x+1]:
#                 arr[x+1] += 1
#                 break
#             elif arr[i] > arr[x+1]:
#                 arr[x+1] += 1
#             else: break
#     print(arr)
#     print(sum(arr))

'''
4
3
3
2
3
'''

def getMinimumUniqueSum(arr):
    setlist = set()

    for e in arr:
        if e not in setlist:
            setlist.add(e)
        else:
            while e in setlist:
                e += 1
            setlist.add(e)

    print(sum(setlist))




if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMinimumUniqueSum(arr)


