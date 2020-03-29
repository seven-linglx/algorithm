#!/usr/bin/env python
"""给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与
target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。例如，给定数组 nums = [-1，2，1，-4],
和 target = 1. 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def three_sum_closest(self, nums, target) -> int:
        nums.sort()
        length = len(nums)
        gap = 99999
        closest = None
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = length - 1
            while start < end:
                sum_temp = nums[i] + nums[start] + nums[end]
                gap_temp = abs(sum_temp - target)
                if sum_temp < target:
                    start += 1
                    if gap_temp < gap:
                        closest = sum_temp
                        gap = gap_temp
                elif sum_temp == target:
                    return target
                else:
                    end -= 1
                    if gap_temp < gap:
                        closest = sum_temp
                        gap = gap_temp
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                break
            if nums[i] + nums[-2] + nums[-1] < target:
                continue
        return closest


def test():
    solu = Solution()
    assert solu.three_sum_closest([-1, 2, 1, -4], 1) == 2
    assert solu.three_sum_closest([-1, 2, 1, 3, -4, 5], 8) == 8
    assert solu.three_sum_closest([-1, 2, 1, 3, -4, 5], -1) == -1


if __name__ == '__main__':
    solu = Solution()
    print(solu.three_sum_closest([-1, 2, 1, -4], 1))
