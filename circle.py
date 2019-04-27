# -*- coding: utf-8 -*-
"""
判断一个有向图是否存在环
有一个有向图，每个元素代表一个边，元素的第一个值为父节点，第二个值为子节点
如果任意一个节点往子节点走下去又能回到当前节点则存在环，实现函数，判断是否存在环。
[{A,B}, {B,C}, {A,C}] 无环
[{A,B}, {B,C}, {A,C}, {C, A}] 有环
"""
import re


def transform(input):
    _input = input.upper()
    _input = re.sub("[^A-Z]", "", _input)
    _result = []
    for i in range(0, len(_input), 2):
        f = _input[i]
        s = _input[i + 1]
        _result.append((f, s))
    return _result


def dsf(input, current, loop):
    if loop[-1][1] == current[0]:
        loop.append(current)
        # 有环，则返回成功标致
        if loop[-1][1] == loop[0][0]:
            return True

    if len(input) == 0 and len(loop) > 1:
        loop.pop()

    for j, single in enumerate(input):
        res = dsf(input[j + 1:] + input[:j], single, loop)
        # 这里很关键，需要把后面的递归结果传到前面
        if res:
            return True
    # 如果递归结束，还没有检测到，则返回False
    return False


def detect(input):
    _input = transform(input)
    result = []
    # 每个元素都使用‘深度优先搜索’检测是否存在环，并记录结果
    for i, single in enumerate(_input):
        loop = [single]
        input_single = _input[:i] + _input[i+1:]
        result.append(dsf(input_single, single, loop))
    # '''
    # DEGUB
    for j, res in enumerate(result):
        # 查看具体哪个元素不能找到环
        if res is False:
            print(_input[j])
    # '''
    # 有一个元素不存在环，则整个图不存在环
    if False in result:
        return False
    else:
        return True


if __name__ == "__main__":
    # example = input()
    example = '[{A,B},{B,C},{c,a},{d,a},{a,C},{C,B}]'
    result = detect(example)
