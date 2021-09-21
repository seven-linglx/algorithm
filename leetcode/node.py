#!/usr/bin/env python


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_node(l: list) -> ListNode:
    root = pre = ListNode()
    for num in l:
        pre.next = ListNode(num)
        pre = pre.next
    return root.next


def node_to_list(root: ListNode) -> list:
    cur = root
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res
