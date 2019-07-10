# -*- coding: utf-8 -*-
# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        sum = x
        y = 0
        while sum:
            y = y * 10 + sum % 10
            sum = sum / 10
        return y == x