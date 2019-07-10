# -*- coding: utf-8 -*-
# Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = [None]
        y = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in y:
                if y[c] != x.pop():
                    return False
            else:
                x.append(c)
        return len(x) == 1