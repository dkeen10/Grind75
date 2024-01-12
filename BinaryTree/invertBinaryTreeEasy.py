# https://leetcode.com/problems/invert-binary-tree/description/

"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:
    def invertTreeWithoutRecursion(self, root: [TreeNode]) -> [TreeNode]:
        """
        O(n) time complexity since only loops once.
        """
        if root is None:
                return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
     

    def invertTreeWithRecursion(self, root: [TreeNode]) -> [TreeNode]:
        if root is None:
            return root
        root.left, root.right = self.invertTreeWithRecursion(root.right), self.invertTreeWithRecursion(root.left)
        return root
   

def main():
    # root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().invertTreeWithoutRecursion(root)) 
    print(Solution().invertTreeWithRecursion(root))


if __name__ == "__main__":
    main()

