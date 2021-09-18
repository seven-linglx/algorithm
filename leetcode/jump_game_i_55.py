#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个下标。
    """

    def jump(self, nums: List[int]) -> bool:
        """
        1 <= nums.length <= 3 * 10^4
        0 <= nums[i] <= 10 ^ 5
        """
        length = len(nums)
        if length == 1:
            return True
        current = 0
        while (current + nums[current]) < (length - 1):
            max_index = max_step = nums[current]
            # 以当前为起点,找到能跳得最远的点,下次以找到的点为起点
            for i in range(1, nums[current] + 1):
                if (current + i) < length and (nums[current + i] + i) > max_step:
                    max_step = nums[current + i] + i
                    max_index = i
            if max_index == 0:
                return False
            current += max_index
            # print(current)
        return True


def test():
    solution = Solution()
    assert solution.jump([2, 3, 1, 1, 4]) is True
    assert solution.jump([2, 3, 0, 1, 4]) is True
    assert solution.jump([1]) is True
    assert solution.jump([1, 1]) is True
    assert solution.jump([1, 1, 1]) is True
    assert solution.jump([2, 1]) is True
    assert solution.jump([2, 3, 2, 4, 1, 4]) is True
    assert solution.jump([2, 3, 2, 4, 3, 1, 4]) is True
    assert solution.jump([1, 2, 1, 1, 1]) is True
    assert solution.jump([4, 1, 1, 3, 1, 1, 1]) is True
    assert solution.jump([3, 2, 1, 0, 4]) is False


def main():
    solution = Solution()
    solution.jump([4, 1, 1, 3, 1, 1, 1])


if __name__ == "__main__":
    main()
