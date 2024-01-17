# https://leetcode.com/problems/balanced-binary-tree/

"""
Given a binary tree, determine if it is
height-balanced
.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        return (self.Height(root) >= 0)
        
    def Height(self, root):
        if root is None:
            return True
        leftHeight = self.Height(root.left)
        rightHeight = self.Height(root.right)
        if leftHeight > 0 or rightHeight > 0 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

def main():
    pass


if __name__ == '__main__':
    main()
