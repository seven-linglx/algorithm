#!/usr/bin/env python
"""
给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
形式上，斐波那契式序列是一个非负整数列表 F，且满足：
0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
F.length >= 3；
对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
返回从 S 拆分出来的所有斐波那契式的序列块，如果不能拆分则返回 []。

示例 1：
输入："123456579"
输出：[123,456,579]
示例 2：
输入: "11235813"
输出: [1,1,2,3,5,8,13]
示例 3：
输入: "112358130"
输出: []
解释: 这项任务无法完成。
示例 4：
输入："0123"
输出：[]
解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
示例 5：
输入: "1101111"
输出: [110, 1, 111]
解释: 输出 [11,0,11,11] 也同样被接受。
提示：
1 <= S.length <= 200
字符串 S 中只含有数字。
"""


def split_into_fibonacci(s):
    if len(s) < 3:
        return []

    maxest = 2147483648  # 32位有符号整数类型,2^32 - 1

    def fibonacci(fi, se, string, result: list):
        if len(string) == 0:
            return True
        th = fi + se
        third = str(th)
        if len(third) <= len(string) and th <= maxest and third == string[: len(third)]:
            result.append(th)
            return fibonacci(se, th, string[len(third):], result)
        else:
            return False

    first = second = 0
    length = len(s)
    for i in range(1, length - 1):
        if i > 1 and "0" == s[0]:
            continue
        first = int(s[:i])
        if first > maxest:
            continue
        for j in range(i + 1, length):
            if (j - i) > 1 and "0" == s[i]:
                continue
            second = int(s[i:j])
            if second > maxest:
                continue
            result = [first, second]
            # print(result)
            if fibonacci(first, second, s[j:], result):
                return result
    return []


def check_fibonacci(nums):
    length = len(nums)
    for i in range(2, length):
        if nums[i] != nums[i - 1] + nums[i - 2]:
            return False
    return True


def test():
    assert split_into_fibonacci("11235813") == [1, 1, 2, 3, 5, 8, 13]
    assert split_into_fibonacci("123456579") == [123, 456, 579]
    assert split_into_fibonacci("0123") == []
    assert split_into_fibonacci("10123") == []
    assert split_into_fibonacci("1101111") == [11, 0, 11, 11]
    assert (
        split_into_fibonacci(
            "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
        )
        == []
    )


def test_fibonacci():
    assert (
        check_fibonacci(
            [
                539834657,
                21,
                539834678,
                539834699,
                1079669377,
                1619504076,
                2699173453,
                4318677529,
                7017850982,
                11336528511,
            ]
        )
        is True
    )
