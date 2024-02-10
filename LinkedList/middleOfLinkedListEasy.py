# https://leetcode.com/problems/middle-of-the-linked-list/description/

"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        middle = length // 2

        temp2 = head
        count = 0
        while temp2:
            if count == middle:
                return temp.val
            count += 1
        return -1


def main():
    head = [1, 2, 3, 4, 5]
    print(Solution().middleNode(head))

    head = [1, 2, 3, 4, 5, 6]
    print(Solution().middleNode(head))


if __name__ == "__main__":
    main()
