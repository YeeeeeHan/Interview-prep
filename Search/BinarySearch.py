def BinarySearch(value, sorted_arr):
    x = len(sorted_arr)
    if value == sorted_arr[x//2]:
         return x//2 # returns the index of the value
    elif value < sorted_arr[x//2]:
        return BinarySearch(value, sorted_arr[0:x//2])
    elif value > sorted_arr[x//2]:
        return BinarySearch(value, sorted_arr[x//2+1:x+1])


arr = [2,3,4]

print(BinarySearch(3, arr))


