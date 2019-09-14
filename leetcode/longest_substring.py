#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
"abcabcbb" --> abc --> 3
"bbbbb" --> b --> 1
"pwwkew" --> wke --> 3  "pwke"是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        ans = 0
        for start in range(len(s) - 1):
            substring = set()
            for end in range(start, len(s)):
                substring.add(s[end])
                if len(substring) == (end - start + 1):
                    ans = max(ans, (end - start + 1))
                else:
                    break
        return ans


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        ans = 0
        i = 0
        substring = {}
        while i < len(s):
            if s[i] in substring:
                # assert substring[s[i]] < i
                i = substring[s[i]] + 1
                ans = max(ans, len(substring))
                substring.clear()
            else:
                substring[s[i]] = i
                i = i + 1
        ans = max(ans, len(substring))
        return ans


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        ans = start = 0
        substring = {}
        for i in range(length):
            if s[i] in substring and substring[s[i]] >= start:
                start = substring[s[i]] + 1
            substring[s[i]] = i
            ans = max(ans, (i - start + 1))
        return ans


def test():
    """使用pytest,只需要安装了pytest,再执行pytest filename.py"""
    solution = Solution3()
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    assert solution.lengthOfLongestSubstring("  ") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("bbbb") == 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3


def main():
    solution = Solution3()
    s = "abcabcbb"
    s = "bbbbbbbb"
    s = "pwwkew"
    s = "dvdf"
    print(solution.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()
