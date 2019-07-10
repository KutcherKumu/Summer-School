# -*- coding: utf-8 -*-
# Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = cmp(x, 0) * int(str(abs(x))[::-1])
        return ans if ans.bit_length() < 32 else 0