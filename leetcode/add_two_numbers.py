# -*- coding: utf-8 -*-
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
from node import ListNode, list_to_node, node_to_list


class Solution:
    @staticmethod
    def add_two(a, b, flag):
        # temp_list = (i for i in [a, b, flag] if i is not None)
        # add_sum = sum(temp_list)
        add_sum = a + b + flag
        if add_sum >= 10:
            return add_sum - 10, 1
        else:
            return add_sum, 0

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        add_sum, flag = self.add_two(l1.val, l2.val, flag)
        _start = start = ListNode(add_sum)
        while l1.next is not None or l2.next is not None or flag == 1:
            l1_next_val, l1 = (0, l1) if l1.next is None else (l1.next.val, l1.next)
            l2_next_val, l2 = (0, l2) if l2.next is None else (l2.next.val, l2.next)
            add_sum, flag = self.add_two(l1_next_val, l2_next_val, flag)
            start.next = ListNode(add_sum)
            start = start.next

        return _start

    @staticmethod
    def stdout(l: ListNode):
        res = map(str, node_to_list(l))
        print("->".join(res))

    def test(self):
        l1 = list_to_node([5, 4, 3])
        l2 = list_to_node([5, 6, 4])
        self.stdout(l1)
        self.stdout(l2)
        self.stdout(self.add_two_numbers(l1, l2))


def main():
    solution = Solution()
    solution.test()


if __name__ == "__main__":
    main()
