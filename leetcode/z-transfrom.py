#!/usr/bin/env python
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.default_char = "^"
        self.matrix = self.gen_matrix(self.row, self.col)

    def gen_matrix(self, row, col):
        return [[self.default_char for l in range(col)] for r in range(row)]

    def transform(self):
        result = ""
        for line in self.matrix:
            for ch in line:
                if ch != self.default_char:
                    result += ch
        return result

    def __setitem__(self, t, value):
        row, col = t
        self.matrix[row][col] = value

    def __getitem__(self, t):
        row, col = t
        return self.matrix[row][col]

    def __str__(self):
        matrix_str = []
        for line in self.matrix:
            matrix_str.append("".join(line))
        return "\n".join(matrix_str)


class Solution:
    def compute_col(self, length, row):
        loop = row + row - 2
        col_of_loop = row - 1
        num_of_loop, mod = divmod(length, loop)
        if mod == 0:
            col = num_of_loop * col_of_loop
        elif mod <= row:
            col = num_of_loop * col_of_loop + 1
        else:
            col = num_of_loop * col_of_loop + 1 + (mod - row)
        return loop, col_of_loop, col

    def convert(self, s: str, row: int) -> str:
        if row <= 1:
            return s
        loop, col_of_loop, col = self.compute_col(len(s), row)
        matrix = Matrix(row, col)
        for i, ch in enumerate(s):
            div, mod = divmod(i, loop)
            if mod < row:
                matrix[mod, div * col_of_loop] = ch
            else:
                matrix[
                    (row - 1) - (mod - row + 1), div * col_of_loop + (mod - row + 1)
                ] = ch
        return matrix.transform()


class Solution2:
    def convert(self, s: str, row: int) -> str:
        if row <= 1:
            return s
        rows = [''] * min(len(s), row)
        i = 0
        stride = 1
        for ch in s:
            rows[i] += ch
            if i == 0:
                stride = 1
            if i == row - 1:
                stride = -1
            i += stride
        return ''.join(rows)


def test_compute_col():
    solu = Solution2()
    assert solu.convert("abc", 1) == "abc"
    assert solu.convert("LEETCODEISHIRING", 3) == "LCIRETOESIIGEDHN"
    assert solu.convert("LEETCODEISHIRING", 4) == "LDREOEIIECIHNTSG"


def test_matrix():
    matrix = Matrix(3, 4)
    matrix[1, 1] = "Z"
    assert matrix[1, 1] == 'Z'
