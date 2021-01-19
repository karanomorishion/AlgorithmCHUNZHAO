# 1. Two Sum (Easy)
# https://leetcode-cn.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable.keys():
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []
