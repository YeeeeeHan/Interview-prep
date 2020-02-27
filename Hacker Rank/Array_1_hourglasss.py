# Sample input
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Complete the hourglassSum function below.
def hourglassSum(arr):
    my_list = []
    for row in range(4):
        for column in range(4):
            my_list.append(sum(arr[row][column:column + 3]) + arr[row + 1][column + 1] + sum(arr[row + 2][column:column + 3]))
    print((max(my_list)))

    # list index [:] doesn't take into account out of range
    # cannot sum an int



if __name__ == '__main__':


    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglassSum(arr)





