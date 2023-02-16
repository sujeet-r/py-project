"""
Given an array of integers nums and an integer target, return indices of the two numberssuch that theyadd up to target.

"""
nums= [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target :
            print("[",i,",",j,"]")