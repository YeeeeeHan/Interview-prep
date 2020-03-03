def removeDuplicates(nums) -> int:
    runner = 1
    terminate = nums[-1]
    for i in range(len(nums)):
        if nums[i] == terminate:
            break
        temp = runner
        while nums[i] >= nums[i + temp]:
            temp += 1
        nums[i + 1], nums[i + temp]= nums[i + temp], nums[i + 1]
    print(nums[:i+1])





if __name__ == '__main__':
    nums = [1, 1, 3, 4, 5, 6]
    removeDuplicates(nums)
