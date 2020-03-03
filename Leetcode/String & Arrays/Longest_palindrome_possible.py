from collections import Counter
from pandas import *


def longestPalindrome(s) -> int:
    new = Counter(s)
    length = 0
    for key, value in new.items():
        length += value // 2 * 2
        if length % 2 == 0 and len(s)%2 ==1 :
            length += 1
    print(length)


def longPalindromeSubstring(arr):
    new = list(reversed(arr))
    count = 0
    for i in range(len(arr)):
        for j in range(len(new)):
            length = 0
            if arr[i] != new[j]:
                j+=1
            else:
                tempi = i
                tempj = j
                while (tempi<len(arr) and tempj<len(arr)):
                    if arr[tempi] == new[tempj]:
                        length+=1
                        tempi+=1
                        tempj+=1
                        print(f" tempi:{tempi}, tempj:{tempj}")
                    else:
                        break
                count = max(count,length)
    print(count)


def DP_longestPalindromeSubstring(p, s):
    for i in range(len(s)):
        for j in range(i,len(s)):
            p[i][i] = True
            p[i-1][i] = s[i-1] == s[i]
            print(DataFrame(grid))

    for i in range(len(s)-1):
        for j in range(i, len(s)-1):
            p[i][j]= p[i+1][j-1] and s[i]==s[j]







if __name__ == '__main__':
    s = "abaabc"
    grid = [[False for i in range(len(s))] for i in range(len(s))]
    DP_longestPalindromeSubstring(grid,s)
    print(DataFrame(grid))

