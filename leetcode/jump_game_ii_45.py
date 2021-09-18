#!/usr/bin/env python

from typing import List


class Solution:
    """leetcode 45 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。 数组中的每个元素代表你在该位
    置可以跳跃的最大长度。 你的目标是使用最少的跳跃次数到达数组的最后一个位置。 假设你总是可以到达数组的
    最后一个位置"""

    def jump(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 10^4
        0 <= nums[i] <= 1000
        """
        length = len(nums)
        if length == 1:
            return 0
        current = step = 0
        while (current + nums[current]) < (length - 1):
            max_index = max_step = nums[current]
            # 以当前为起点,找到能跳得最远的点,下次以找到的点为起点
            for i in range(1, nums[current] + 1):
                if (current + i) < length and (nums[current + i] + i) > max_step:
                    max_step = nums[current + i] + i
                    max_index = i
            current += max_index
            # print(current)
            step += 1
        return step + 1


def test():
    solution = Solution()
    assert solution.jump([2, 3, 1, 1, 4]) == 2
    assert solution.jump([2, 3, 0, 1, 4]) == 2
    assert solution.jump([1]) == 0
    assert solution.jump([1, 1]) == 1
    assert solution.jump([1, 1, 1]) == 2
    assert solution.jump([2, 1]) == 1
    assert solution.jump([2, 3, 2, 4, 1, 4]) == 3
    assert solution.jump([2, 3, 2, 4, 3, 1, 4]) == 3
    assert solution.jump([1, 2, 1, 1, 1]) == 3
    assert solution.jump([4, 1, 1, 3, 1, 1, 1]) == 2


def main():
    solution = Solution()
    solution.jump([4, 1, 1, 3, 1, 1, 1])


if __name__ == "__main__":
    main()
