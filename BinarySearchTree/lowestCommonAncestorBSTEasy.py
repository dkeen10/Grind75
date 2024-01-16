# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = left


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        we do DFS and since BST is set up such that for each Node, left descendant is less and right descendant is greater, we can check:
            - If both p and q are greater than the value of temp, move to the right child (temp = temp.right).
            - If both p and q are smaller than the value of temp, move to the left child (temp = temp.left).
            - If the values of p and q are on opposite sides of temp (one is greater, and the other is smaller), temp is the lowest common ancestor. Return temp.
        """

        currentNode = root

        while currentNode is not None:
            if p.val > root.val and q.val > root.val:
                currentNode = currentNode.right
            elif p.val < root.val and q.val < root.val:
                currentNode = currentNode.left
            else:
                return currentNode


def main():
    root = [TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))]
    p = TreeNode(2)
    q = TreeNode(8)
    print(Solution().lowestCommonAncestor(root, p, q))


if __name__ == "__main__":
    main()
