# https://leetcode.com/problems/linked-list-cycle/description/

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycleList(self, head: [ListNode]) -> bool:
        address = []
        currentNode = head
        while (currentNode):
            address.append(currentNode)
            currentNode = currentNode.next
            if (currentNode in address):
                return True
        return False
    

    def hasCycleTwoPointer(self, head: [ListNode]) -> bool:
        fastpointer = head
        slowpointer = head
        while (fastpointer and fastpointer.next):
            fastpointer = fastpointer.next.next
            slowpointer = slowpointer.next
            if (fastpointer == slowpointer):
                return True
        return False
    

    # similar to the list approach, just using a set instead of a list
    def hasCycleHash(self, head: [ListNode]) -> bool:
        visited = set()
        currentNode = head
        while (currentNode):
            if (currentNode in visited):
                return True
            visited.add(currentNode)
            currentNode = currentNode.next


def main():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    pos = 1
    print(Solution().hasCycleList(head)) # True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    pos = 0
    print(Solution().hasCycleList(head)) # True

    head = ListNode(1)
    pos = -1
    print(Solution().hasCycleList(head)) # False

    


if __name__ == '__main__':
    main()

