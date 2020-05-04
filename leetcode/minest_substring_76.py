#!/usr/bin/env python

"""
最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""


def sub(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    target_dict = {}

    for ch in t:
        if ch in target_dict:
            target_dict[ch] += 1
        else:
            target_dict[ch] = 1

    length = len(s)
    end = default = length + 1
    start = j = 0
    count = len(target_dict)
    for i in range(length):
        while j < length and count > 0:
            if s[j] in target_dict:
                target_dict[s[j]] -= 1
                if target_dict[s[j]] == 0:
                    count -= 1
            j += 1
        # j已经在前面多加了个1
        if count == 0 and j - i < end - start:
            start = i
            end = j

        if s[i] in target_dict:
            target_dict[s[i]] += 1
            if target_dict[s[i]] == 1:
                count += 1
    print(target_dict)
    return s[start: end] if start != 0 or end != default else ""


def test():
    assert sub("ADOBECODEBANC", "ABC") == "BANC"
    assert sub("ADOBECODEBANC", "AB") == "BA"
    assert sub("A", "AB") == ""
    assert sub("ADOBECODEBANC", "AC") == "ANC"
    assert sub("CD", "AB") == ""
    assert sub("C", "C") == "C"
    assert sub("AC", "AC") == "AC"
    assert sub("a", "a") == "a"
    assert sub("aa", "aa") == "aa"
