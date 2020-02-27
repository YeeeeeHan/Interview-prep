#!/bin/python3
# SAMPLE INPUT
# 1
# daBcd
# ABC
#
# 1
# ababbaAbAB
# AABABB

import math
import os
import random
import re
import sys
import numpy as np
from pprint import pprint


def abbreviation(a, b):
    print(a)
    print(b)

    T = [[0 for i in range(len(b))] for j in range(len(a))]
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    pprint(T)

    # print(int(T[len(a)-1][len(b)-1]))
    # print(len(b)-1)
    if int(T[len(a)-1][len(b)-1]) == len(b)-1:
        print("True")

    else:
        return("False")





if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        a = list(input().upper())
        a.insert(0,0)

        b = list(input().upper())
        b.insert(0,0)

        result = abbreviation(a, b)


