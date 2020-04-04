#!/usr/bin/env python

"""给出n个数，m个询问，每次询问区间[x,y]中第k小的数是多少。求区间第k小，最简单的就是把数组排序，然后
取下标为k的数，但m次排序后会超时，能否一次排序就解决m个询问呢? 像快排一样，对于区间[l,r]，取
mid=(l+r)/2，把i<=mid的向左放，i>mid的向右放，然后递归处理，在排序的同时记录下排序的过程，询问时按记
录的信息顺藤摸瓜就可以了"""


class PartitionTree:
    def __init__(self, array):
        self.array_sorted = [0] + sorted(array)
        self.length = len(array) + 1
        self.levels = [[0 for j in range(self.length)] for i in range(self.length)]
        self.counts = [[0 for j in range(self.length)] for i in range(self.length)]
        self.levels[0] = [0] + array
        self.build(1, self.length - 1, 0)

    def build(self, start: int, end: int, level: int):
        if start == end:
            return
        mid = (start + end) // 2
        mid_v = self.array_sorted[mid]
        same = mid - start + 1
        for i in range(start, end + 1):
            if self.levels[level][i] < mid_v:
                same -= 1
        left = start
        right = mid + 1
        for i in range(start, end + 1):
            cur_v = self.levels[level][i]
            self.counts[level][i] = self.counts[level][i - 1]
            if cur_v < mid_v or (cur_v == mid_v and same > 0):
                if cur_v == mid_v:
                    same -= 1
                self.levels[level + 1][left] = self.levels[level][i]
                left += 1
                self.counts[level][i] += 1
            else:
                self.levels[level + 1][right] = self.levels[level][i]
                right += 1
        self.build(start, mid, level + 1)
        self.build(mid + 1, end, level + 1)

    def query(self, start, end, k, lbound, rbound, level=0):
        if end - start + 1 < k:
            raise ValueError("输入的区间与第k大数不匹配")
        if start == end:
            return self.levels[level][start]
        mid = (lbound + rbound) >> 1
        x = self.counts[level][start - 1] - self.counts[level][lbound - 1]
        y = self.counts[level][end] - self.counts[level][lbound - 1]
        cnt = y - x
        nx = start - lbound - x  # start - 1位于右子树的数量
        ny = end - lbound - y  # end位于右子树的数量
        if cnt >= k:
            return self.query(lbound + nx, lbound + y - 1, k, lbound, mid, level + 1)
        else:
            return self.query(
                mid + 1 + nx, mid + 1 + ny, k - cnt, mid + 1, rbound, level + 1
            )


def test():
    pt = PartitionTree([4, 3, 9, 2, 5, 7, 1, 8, 3, 6])
    assert pt.query(2, 5, 1, 1, pt.length - 1, 0) == 2
    assert pt.query(2, 3, 1, 1, pt.length - 1, 0) == 3
    assert pt.query(3, 8, 1, 1, pt.length - 1, 0) == 1


if __name__ == "__main__":
    pt = PartitionTree([4, 2, 5, 7, 1, 8, 3, 6])
    print(pt.levels)
    print(pt.counts)
