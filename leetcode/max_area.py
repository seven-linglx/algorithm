#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给出一个整数序列，找出其最大面积
"""


class Solution:
    def max_area(self, heights: list) -> int:
        area = 0
        numbers = len(heights)
        for i in range(numbers):
            for j in range(i, numbers):
                temp = (j - i) * min(heights[i], heights[j])
                if temp > area:
                    area = temp
        return area


class Solution2:
    def max_area(self, heights: list) -> int:
        area = 0
        end = len(heights) - 1
        start = 0
        while start < end:
            area = max((end - start) * min(heights[start], heights[end]), area)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return area


def test():
    solu = Solution2()
    assert solu.max_area([2, 3, 4, 5]) == 6
    assert solu.max_area([3, 7, 4, 5]) == 10
    assert solu.max_area([1, 9, 8, 6, 2, 5, 4, 8, 3, 7]) == 56
