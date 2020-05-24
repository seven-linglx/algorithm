#!/usr/bin/env python
"""
给定一个整数数组 A，返回 A 中最长等差子序列的长度。
回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length -
1。并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。
示例 1：
输入：[3,6,9,12]
输出：4
解释：
整个数组是公差为 3 的等差数列。
示例 2：
输入：[9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。
示例 3：
输入：[20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。
提示：
2 <= A.length <= 2000
0 <= A[i] <= 10000
"""


def longest_arith_seq_len(nums: list) -> int:
    length = len(nums)
    dp = [None] * length
    for i in range(length):
        dp[i] = {}
    res = 2
    for i in range(1, length):
        for j in range(0, i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                res = max(res, dp[i][diff])
            else:
                dp[i][diff] = 2
    # print(dp)
    return res


def test():
    assert longest_arith_seq_len([9, 4, 7, 2, 10]) == 3
    assert longest_arith_seq_len([9, 4]) == 2
    assert longest_arith_seq_len([2, 4]) == 2
    assert longest_arith_seq_len([2, 4, 6]) == 3
    assert longest_arith_seq_len([3, 6, 9, 12]) == 4
    assert longest_arith_seq_len([20, 1, 15, 3, 10, 5, 8]) == 4
    assert longest_arith_seq_len([3, 6, 9, 12, 15, 21, 27]) == 5
