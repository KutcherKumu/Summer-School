# -*- coding: utf-8 -*-
# Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        sum = list[s[len(s)-1]]
        for i in xrange(len(s)-1, 0, -1):
            x = list[s[i]]
            y = list[s[i-1]]
            sum += y if y >= x else -y
        return sum