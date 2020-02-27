#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp = [None for i in range(len(arr))]

    if len(arr) == 1:
        return arr[0]

    elif len(arr) == 2:
        return max(arr[0],arr[1])

    else:
        dp[0] = arr[0]
        dp[1] = max(arr[0],arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], dp[i-2], dp[i-2] + arr[i], arr[i])
    return dp[len(arr)-1]





if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr,n)

    print(str(res) + '\n')

