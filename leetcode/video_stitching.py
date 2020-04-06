#!/usr/bin/env python
"""你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可
能长度不一。视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可
以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。我们需要将这些
片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果
无法完成该任务，则返回 -1 。

"""


class Solution:
    """递归穷举求解"""
    count_max = 9999
    count = count_max

    def stitching(self, clips, stack, e):
        if stack[-1][1] >= e:
            self.count = min(self.count, len(stack) - 1)
            print(stack)

        for i in range(len(clips)):
            if stack[-1][0] <= clips[i][0] <= stack[-1][1]:
                stack.append(clips[i])
                self.stitching(clips[:i] + clips[i + 1:], stack, e)
                stack.pop()

    def video_stitching(self, clips, T):
        self.count = self.count_max
        stack = [[0, 0]]
        self.stitching(clips, stack, T)
        return -1 if self.count == self.count_max else self.count


class Solution2:
    """贪心算法求解"""

    def video_stitching(self, clips: list, T: int) -> int:
        clips = sorted(clips, key=lambda x: (x[0], x[0] - x[1]), reverse=False)
        print(clips)
        length = len(clips)
        if clips[0][0] > 0:
            return -1
        s = i = j = max_clip = count = 0
        while i < length:
            if max_clip >= T:
                break
            while j < length and clips[j][0] <= s:
                max_clip = max(max_clip, clips[j][1])
                j += 1
            if i == j:
                return -1
            s = max_clip
            count += 1
            i = j
        return -1 if max_clip < T else count


def test():
    solu = Solution2()
    assert (solu.video_stitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10) == 3)
    assert solu.video_stitching([[0, 1], [1, 2]], 5) == -1
    assert (solu.video_stitching(
        [
            [0, 1],
            [6, 8],
            [0, 2],
            [5, 6],
            [0, 4],
            [0, 3],
            [6, 7],
            [1, 3],
            [4, 7],
            [1, 4],
            [2, 5],
            [2, 6],
            [3, 4],
            [4, 5],
            [5, 7],
            [6, 9],
        ],
        9,
    ) == 3)


if __name__ == '__main__':
    solu = Solution2()
    v = solu.video_stitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10)
    print(v)
