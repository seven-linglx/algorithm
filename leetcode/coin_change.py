#!/usr/bin/env python
"""
零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个
数。如果没有任何一种硬币组合能组成总金额，返回 -1。示例 1:输入: coins = [1, 2, 5], amount = 11输出:
3 解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。
"""


class Solution:
    """
    动态规划
    f(x) = 1 + min(f(x-k[0]), f(x-k[1]), ..., f(x-k[n]))
    """
    @staticmethod
    def coin_change(coins, amount):
        length = amount + 1
        maxest = 999999
        dp = [maxest] * length
        dp[0] = 0
        for i in range(1, length):
            # a = [dp[i - j] if j <= i else maxest for j in coins]
            # print(a)
            dp[i] = 1 + min(dp[i - j] if j <= i else maxest for j in coins)
        return -1 if dp[-1] >= maxest else dp[-1]


def test():
    solution = Solution()
    assert solution.coin_change([1, 2, 5], 11) == 3
    assert solution.coin_change([1, 2, 5], 2) == 1
    assert solution.coin_change([2], 3) == -1
    assert solution.coin_change([2, 3, 4, 5, 7, 9, 10], 12) == 2


if __name__ == '__main__':
    test()
