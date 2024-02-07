# https://leetcode.com/problems/reverse-linked-list/description/

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_3Pointer(self, head: [ListNode]) -> [ListNode]:
        """
        uses 3 pointers to iterate through the linked list, swapping the direction of the links.
        reversed_head -> points to head of reversed linked list
        current_head -> traverses the linked list and reverses each node's next pointer.
        next_node -> points to the next node in the original"""
        reversed_head = None
        current_head = head

        # run loop until current_head points to None
        while current_head:
            # initialize next pointer to next node of current head
            next_node = current_head.next

            # swap current_head's next node to previous node
            current_head.next = reversed_head

            # iterate by assigning current_head to previous head (reversed) and current_head to next node in list.
            reversed_head = current_head
            current_head = next_node

        return reversed_head
            


    def reverseList_Recursive(self, head: [ListNode]) -> [ListNode]:
        pass

def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().reverseList_3Pointer(head))


if __name__ == "__main__":
    main()


        