def getMinimumUniqueSum(arr):
#     area of water = min(arr[x],arr[y]) * y-x

    # area = 0
    # for i in range(len(arr)-1):
    #     for j in range(i+1, len(arr)):
    #         temp = min(arr[i], arr[j]) * abs(j-i)
    #         if  temp >= area:
    #             area = temp
    # print(area)

    area = 0
    s = 0
    e = len(arr)-1
    for i in range(len(arr)-2):
        if arr[s] <= arr[e]:
            area = max(area, arr[s]*(e-s))
            s += 1
        else:
            area = max(area, arr[e] * (e-s))
            e -= 1
    print(area)



if __name__ == '__main__':

    arr = list(map(int, input().strip().split(',')))



    getMinimumUniqueSum(arr)


