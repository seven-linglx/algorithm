#!/usr/bin/env python
from node import ListNode, list_to_node, node_to_list


class Solution:
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two lists"""
        root = pre = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = ListNode(l1.val)
                l1 = l1.next
            else:
                pre.next = ListNode(l2.val)
                l2 = l2.next
            pre = pre.next

        if l1:
            pre.next = l1

        if l2:
            pre.next = l2

        return root.next


def test():
    solution = Solution()
    # fmt:off
    assert node_to_list(solution.merge(list_to_node([1, 2, 4]), list_to_node([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert node_to_list(solution.merge(list_to_node([1, 2, 4]), list_to_node([1, 3, 4, 5]))) == [1, 1, 2, 3, 4, 4, 5]
    assert node_to_list(solution.merge(list_to_node([]), list_to_node([]))) == []
    assert node_to_list(solution.merge(list_to_node([]), list_to_node([0]))) == [0]
    assert node_to_list(solution.merge(list_to_node([1]), list_to_node([0]))) == [0, 1]
    # fmt:on


def main():
    root = list_to_node([1, 2, 3, 4, 5, 6])
    print(node_to_list(root))


if __name__ == "__main__":
    main()
