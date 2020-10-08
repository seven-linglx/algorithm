#!/usr/bin/env python
"""
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
示例 1:
输入: [1,2,3]

       1
      / \
     2   3
输出: 6

示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
输出: 42
"""
import collections


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_bt(nums) -> TreeNode:
    root = TreeNode(nums[0])
    dq = collections.deque()
    dq.append(root)
    for i in range(1, len(nums), 2):
        current = dq.popleft()
        if nums[i]:
            left = TreeNode(nums[i])
            dq.append(left)
            current.left = left
        if nums[i + 1]:
            right = TreeNode(nums[i + 1])
            dq.append(right)
            current.right = right

    return root


def preorder_traversal(root: TreeNode):
    if not root:
        return
    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root: TreeNode, ans):
    if not root:
        return 0
    left_max = max(0, postorder_traversal(root.left, ans))
    right_max = max(0, postorder_traversal(root.right, ans))
    ans[0] = max(ans[0], left_max + right_max + root.val)
    return max(left_max, right_max) + root.val


def inorder_traversal(root: TreeNode, values: list, max_value: list):
    """有漏解"""
    if not root:
        return
    inorder_traversal(root.left, values, max_value)
    if sum(values) + root.val > 0:
        values.append(root.val)
    else:
        max_value[0] = max(max_value[0], sum(values))
        values.clear()
    inorder_traversal(root.right, values, max_value)


def test_build_bt():
    preorder_traversal(build_bt([1, 2, 3]))
    preorder_traversal(build_bt([-10, 9, 20, None, None, 15, 7]))


def max_path_sum(root: TreeNode) -> int:
    max_value = [-99999]
    postorder_traversal(root, max_value)
    return max_value[0]


def test():
    assert max_path_sum(build_bt([1, 2, -3])) == 3
    assert max_path_sum(build_bt([-10, 9, 20, None, None, 15, 7])) == 42
    assert max_path_sum(build_bt([-5, 9, 20, None, None, 15, 7])) == 42
    assert max_path_sum(build_bt([-5, 20, 20, None, None, 15, 7])) == 50
    assert max_path_sum(build_bt([-10, 20, 9, 15, 7, None, None])) == 42
