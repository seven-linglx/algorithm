#!/usr/bin/env python
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        step = 0
        while step < n:
            fast = fast.next
            step += 1
        # 如果fast为None，说明要删除的就是根节点，直接返回根节点的下一个节点
        if not fast:
            return head.next
        # 使用fast.next是让slow停在删除节点的前一个
        while fast.next:
            fast = fast.next
            slow = slow.next
        # print(slow.val)
        slow.next = slow.next.next
        return head


def build(nums):
    next_node = head = ListNode(nums[0])
    for i in range(1, len(nums)):
        next_node.next = ListNode(nums[i])
        next_node = next_node.next
    return head


def output(head):
    result = []
    next_node = head
    while next_node:
        result.append(next_node.val)
        next_node = next_node.next
    return result


def test():
    solu = Solution()
    assert output(build([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert output(build([1, 2])) == [1, 2]
    assert output(solu.remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert output(solu.remove_nth_from_end(build([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4]
    assert output(solu.remove_nth_from_end(build([1]), 1)) == []
    assert output(solu.remove_nth_from_end(build([1, 2]), 1)) == [1]
