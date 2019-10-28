# Binary Search Algarithm :
def Binary_Search(nums):
    # take for loop and iterate each one
    for i in range(len(nums)-1,0,-1):
        # take inner for loop ...because of the swap the elements
        for j in range(i):
            # take if condiion and compare the elements
            if(nums[j]>nums[j+1]):
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp



nums = [5,8,6,9,4,2,1,9]
nums.sort()
print(nums)
