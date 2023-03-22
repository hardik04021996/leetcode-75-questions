""" https://leetcode.com/problems/two-sum """

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """ return indices of the two numbers such that they add up to target """
    position = {}
    for i, number in enumerate(nums):
        complement = target - number
        if complement in position:
            return [position[complement], i]
        position[number] = i
        return [-1]

print(two_sum([1,2,3,4],3))
