# -*- coding: utf-8 -*-
# Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = 0
        for i in nums:
            x = x + 1
            if target - i in nums[x:]:
                return(x - 1, nums[x:].index(target - i) + x)