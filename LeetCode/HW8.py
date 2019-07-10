# -*- coding: utf-8 -*-
# Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[ans]:
                ans += 1
                nums[ans] = nums[i]
        return ans+1