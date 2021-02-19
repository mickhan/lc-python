#!/usr/bin/python3
# coding=utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None and root2 == None:
            return None
        elif root1 == None:
            return root2
        elif root2 == None:
            return root1
        else:
            node = TreeNode()
            node.val = root1.val + root2.val
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node

        


def print_tree(root: TreeNode):
    if root == None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

def main():
    s = Solution()
    tA1 = TreeNode(1)
    tA2 = TreeNode(3)
    tA3 = TreeNode(2)
    tA4 = TreeNode(5)
    tA1.left = tA2
    tA1.right = tA3
    tA2.left = tA4
    tB1 = TreeNode(2)
    tB2 = TreeNode(1)
    tB3 = TreeNode(3)
    tB4 = TreeNode(4)
    tB5 = TreeNode(7)
    tB1.left = tB2
    tB1.right = tB3
    tB2.right = tB4
    tB3.right = tB5
    print_tree(s.mergeTrees(tA1, tB1))

if __name__ == "__main__":
    main()
