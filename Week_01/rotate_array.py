# 189. Rotate Array (Easy)
# https://leetcode-cn.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[::-1]
        nums[:k%n] = nums[:k%n][::-1]
        nums[k%n:] = nums[k%n:][::-1]