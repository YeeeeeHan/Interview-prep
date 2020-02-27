#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_dict = {x}

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input().split

        s2 = input().split

        result = twoStrings(s1, s2)

        s1dict = {}
        s2dict = {}

        for element in s1:
            if s1dict.get(element) is not None:  # if key exists
                s1dict[element] += 1  # increment key count by 1

            else:
                s1dict[element] = 1  # else is key doesn't exist, initialise value w 1

        for element in s2:
            if s1dict.get(element) is not None:  # if key exists
                s1dict[element] += 1  # increment key count by 1

            else:
                s1dict[element] = 1  # else is key doesn't exist, initialise value w 1





