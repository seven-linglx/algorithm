#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n > 0:
            return float("%0.5f" % (x * self.myPow(x, n - 1)))
        else:
            return float("%0.5f" % (1.0 / self.myPow(x, -n)))


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        return float("%0.5f" % (self.compute(x, n)))

    # 本质上还是乘了n次
    def compute(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n > 0:
            if n % 2 == 0:
                return self.compute(x, n // 2) * self.compute(x, n // 2)
            else:
                return x * self.compute(x, n - 1)
        else:
            return 1.0 / self.compute(x, -n)


class Solution3:
    def myPow(self, x: float, n: int) -> float:
        return float("%0.5f" % (self.compute(x, n)))

    # 本质上还是乘了n次
    def compute(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n > 0:
            if n % 2 == 0:
                return self.compute(x * x, n // 2)
            else:
                return x * self.compute(x * x, (n - 1) // 2)
        else:
            return 1.0 / self.compute(x, -n)


def test():
    solu = Solution3()
    assert solu.myPow(2.0, 10) == 1024.00
    assert solu.myPow(2.1, 3) == 9.26100
    assert solu.myPow(2.0, -2) == 0.25
    assert solu.myPow(0.44528, 0) == 1.000
    assert solu.myPow(8.88023, 3) == 700.28148
