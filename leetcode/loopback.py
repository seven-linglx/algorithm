#!/usr/bin/env python
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""


def longest_palindrome(s):
    length = len(s)
    if length < 2:
        return s
    dp = [[False for l in range(length)] for r in range(length)]
    start = 0
    end = 0
    max_length = 1
    for right in range(length):
        for left in range(right):
            if s[left] == s[right]:
                if right - left < 3:
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left + 1][right - 1]
            else:
                dp[left][right] = False

            if dp[left][right] and (right - left + 1) > max_length:
                max_length = right - left + 1
                start = left
                end = right
    return s[start: end + 1]


def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("cbabcbabd") == "babcbab"
    assert longest_palindrome("abcde") == "a"
    assert longest_palindrome("a") == "a"
