#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def two_sum(self, nums: list, target: int) -> list:
        big = []
        small = []
        negative = []
        for i in nums:
            if i <= 0:
                negative.append(i)
            elif i < target:
                small.append(i)
            else:
                big.append(i)
        for i in negative:
            for j in big:
                if i + j == target:
                    return [i, j]
        for idx, i in enumerate(small[: len(small) - 1]):
            for j in small[idx + 1 :]:
                if i + j == target:
                    return [i, j]


class Solution2:
    def two_sum(self, nums: list, target: int) -> list:
        # nums = sorted(nums)
        for idx, i in enumerate(nums[: len(nums) - 1]):
            for jdx, j in enumerate(nums[idx + 1 :]):
                if i + j == target:
                    return [idx, idx + 1 + jdx]


class Solution3:
    def two_sum(self, nums: list, target: int) -> list:
        nums_hash = {}
        for i, val in enumerate(nums):
            if (target - val) in nums_hash:
                return [nums_hash[target - val], i]
            nums_hash[val] = i


def test():
    solution = Solution3()
    assert solution.two_sum([3, 3], 6) == [0, 1]


def main():
    solution = Solution3()
    print(solution.two_sum([3, 3], 6))


if __name__ == "__main__":
    main()
