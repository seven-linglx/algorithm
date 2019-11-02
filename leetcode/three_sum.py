#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def three_sum(nums: list, target: int = 0):
        if nums is None and len(nums) < 3:
            return []
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                break
            if nums[i] + nums[-2] + nums[-1] < target:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum_temp = nums[i] + nums[start] + nums[end]
                if sum_temp < target:
                    start += 1
                elif sum_temp == target:
                    results.append([nums[i], nums[start], nums[end]])

                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

                    end -= 1
                    while nums[end] == nums[end + 1] and end > start:
                        end -= 1
                else:
                    end -= 1
        return results


def main():
    solu = Solution()
    print(solu.three_sum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    main()
