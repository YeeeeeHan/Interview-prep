
def func(arr1, arr2):
    count = 0
    a = 0
    b = 0

    while(a!=len(arr1) and b!=len(arr2)):
        if arr1[a] > arr2[b]:
            b+=1
        if arr1[a] < arr2[b]:
            a+=1
        if arr1[a] == arr2[b]:
            count+=1
            a+=1
            b+=1
    print(count)


if __name__ == '__main__':

    arr1 = list(map(int, input().strip().split(',')))
    arr2 = list(map(int, input().strip().split(',')))


    func(arr1,arr2)



