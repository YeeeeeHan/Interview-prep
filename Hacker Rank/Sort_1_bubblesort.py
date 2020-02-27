#!/bin/python3

import math
import os
import random
import re
import sys

# 3
# 3 2 1

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:  # swaps if left > right
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
                count += 1
    print(f"Array is sorted in {count} swaps.")
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
