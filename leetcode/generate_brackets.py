#!/usr/bin/env python
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
start: 22:10
end: 11:14
"""


class Solution:
    """存在很多重复组合，n较大时就会超时"""

    def find_place(self, parenthesis, brackets, length):
        if " " not in brackets:
            parenthesis.add("".join(brackets))
            return
        for start in range(length):
            if brackets[start] != " ":
                continue

            for end in range(start + 1, length):
                # 括号开始和结束之间不能不括号
                if brackets[end] != " ":
                    break
                # 括号开始到结束之间的距离需要是偶数
                if (end - start - 1) % 2 != 0:
                    continue
                else:
                    brackets[start] = "("
                    brackets[end] = ")"
                    self.find_place(parenthesis, brackets, length)
                    # 这交循环设的值要复位
                    brackets[start] = " "
                    brackets[end] = " "

    def generate_parenthesis(self, n):
        parenthesis = set()
        lentgh = 2 * n
        brackets = [" "] * lentgh
        self.find_place(parenthesis, brackets, lentgh)
        return parenthesis


class Solution2:
    """找到规律，用递归方式，当n>=4后，答案不全"""

    def generate_parenthesis(self, n):
        if n == 1:
            return ["()"]
        results = []
        for i in self.generate_parenthesis(n - 1):
            if "()" + i == i + "()":
                results.append(i + "()")
            else:
                results.append("()" + i)
                results.append(i + "()")
            results.append("(" + i + ")")
        return results


class Solution3:
    """动态规划思想"""

    def generate_parenthesis(self, n):
        # 给默认值
        results = [[] for _ in range(n + 1)]
        # 当n为0时,直接给值
        results[0] = [""]
        for i in range(1, n + 1):
            for j in range(i):
                for left in results[j]:
                    for right in results[i - j - 1]:
                        results[i].append(left + "(" + right + ")")
                        # 效果一样
                        # results[i].append("(" + left + ")" + right)
        return results[n]


def test():
    solu = Solution3()
    assert set(solu.generate_parenthesis(1)) == set(["()"])
    assert set(solu.generate_parenthesis(2)) == set(["()()", "(())"])
    assert set(solu.generate_parenthesis(3)) == set(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )
    assert set(solu.generate_parenthesis(4)) == set(
        [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ]
    )


if __name__ == "__main__":
    solu = Solution3()
    solu.generate_parenthesis(3)
