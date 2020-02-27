#!/bin/python3

import math
import os
import random
import re
import sys


'''
5
1 -3 71 68 17
'''


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    minabs = float("inf")
    for i in range(len(arr)-1):
        minabs = min(minabs, abs(arr[i]-arr[i+1]))
    print(arr)
    print(minabs)



if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

