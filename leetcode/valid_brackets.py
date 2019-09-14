#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


class Solution:
    def check(self, a, b):
        if a + b in ("()", "{}", "[]"):
            return True
        else:
            return False

    def is_valid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for char in s:
            if len(stack) != 0 and self.check(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False


def test():
    solu = Solution()
    assert solu.is_valid("(){}[]") is True
    assert solu.is_valid("({}[]") is False
    assert solu.is_valid("{[]}") is True
    assert solu.is_valid("(]") is False
    assert solu.is_valid(")]") is False
    assert solu.is_valid("[)]") is False
