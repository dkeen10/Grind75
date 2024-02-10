# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        pass


def main():
    root = [3, 9, 20, None, None, 15, 7]
    print(Solution().maxDepth(root))

    root = [1, None, 2]
    print(Solution().maxDepth(root))


if __name__ == "__main__":
    main()


