#!/bin/python3

def checkMagazine(magazine, note):
    c = {}
    magazine_set = set(magazine)
    for key in magazine_set:
        c.update({key:magazine.count(key)})
    print(c)
    # c = Counter(magazine)

    for e in note:
        if c.get(e,-1) <= 0:
            print("No")
            return -1
        else:
            c[e] -= 1
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
