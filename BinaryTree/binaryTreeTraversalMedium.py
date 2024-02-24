# https://leetcode.com/problems/binary-tree-level-order-traversal/description/


"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

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

class Solution:
    def levelOrder(self, root: [TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        queue = [root]
        res = []
        
        while queue:
            level = []
            next_queue = []
            
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                    
            res.append(level)
            queue = next_queue    
        return res


def main():
    root = [3,9,20,None,None,15,7]
    sol = Solution()
    print(sol.levelOrder(root))




if __name__ == "__main__":
    main()