""" https://leetcode.com/problems/contains-duplicate/ """

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """ check if an array contains any duplicate in linear time """
    return len(set(nums)) != len(nums)

def contains_duplicate_space_saver(nums: List[int]) -> bool:
    """ check if an array contains any duplicate without using set """
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(contains_duplicate([1,2,3,4,1]))
print(contains_duplicate_space_saver([1,2,3,4,1]))
