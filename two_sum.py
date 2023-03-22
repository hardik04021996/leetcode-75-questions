
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    position = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if(complement in position):
            return [position[complement], i]
        position[nums[i]] = i

print(two_sum([1,2,3,4],3))
