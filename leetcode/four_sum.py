#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组
"""


class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        results_tuple = []
        currents = []
        self.step2(nums, currents, results_tuple, target)
        results_set = [set(a) for a in results_tuple]
        results_set_uniq = []
        results_tuple_final = []

        for i, single_set in enumerate(results_set):
            if single_set not in results_set_uniq:
                results_tuple_final.append(results_tuple[i])
                results_set_uniq.append(single_set)
        print(results_tuple_final)

    def step(self, nums: list, currents: list, results: list, target: int):
        if len(currents) == 4:
            if sum(currents) == target:
                results.append(tuple(currents))
            return True
        for i, cur in enumerate(nums):
            currents.append(cur)
            if self.step(nums[i + 1:], currents, results, target):
                currents.pop()
        if len(currents) != 0:
            currents.pop()

    def step2(self, nums: list, currents: list, results: list, target: int):
        for i, cur in enumerate(nums):
            currents.append(cur)
            if len(currents) == 4:
                if sum(currents) == target:
                    results.append(tuple(currents))
                currents.pop()
            else:
                self.step2(nums[i + 1:], currents, results, target)
        if len(currents) != 0:
            currents.pop()


class Solution2:
    def four_sum(self, nums: list, target: int):
        if nums is None or len(nums) < 4:
            return []
        nums.sort()
        results = []
        # print(nums)
        length = len(nums)
        end = length - 1
        for i in range(0, length - 3):
            # 去除重复值nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 当前循环的边界条件，循环都不用执行了
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 判断当前，后面循环不用执行了
            if nums[i] + nums[end - 2] + nums[end - 1] + nums[end] < target:
                continue
            for j in range(i + 1, length - 2):
                # 去除重复的nums[j]
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                # 当前循环的边界条件，循环都不用执行了
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # 判断当前，后面的循环都不用执行了
                if nums[i] + nums[j] + nums[end - 1] + nums[end] < target:
                    continue
                left = j + 1
                right = end
                while left < right:
                    sum_temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_temp < target:
                        left += 1
                        # 如果和之前的nums[left]一样，没必要计算，肯定 < target
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                    elif sum_temp == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        # 如果和之前的nums[left]一样，没必要计算，肯定 < target
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                        right -= 1
                        # 如果和之前的nums[right]一样，没必要计算，肯定  < target
                        while nums[right] == nums[right + 1] and right > left:
                            right -= 1
                    else:
                        right -= 1
                        # 如果和之前的nums[right]一样，没必要计算，肯定  < target
                        while nums[right] == nums[right + 1] and right > left:
                            right -= 1
        return results


def main():
    solu = Solution2()
    # print(solu.fourSum([-1, 0, -1, 0, -2, 2], 0))
    print(solu.four_sum([-5, 5, 4, -3, 0, 0, 4, -2], 4))
    # print(solu.fourSum([-3, 5, 3, -1, 5, -2, 0, -1], 3))


if __name__ == "__main__":
    main()
