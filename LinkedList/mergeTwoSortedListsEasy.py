# https://leetcode.com/problems/merge-two-sorted-lists/


# given
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        """
        Time complexity: O(n) since each element gets looked at once.
        """
        # edge cases
        if not list1:
            return list2
        if not list2:
            return list1

        # initialize pointers
        p1 = list1
        p2 = list2
        mergedList = ListNode()
        p3 = mergedList

        # loop until both lists are empty
        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next

            # move p3 forward
            p3 = p3.next

        # if one list is empty, append the other
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2

        # return the merged list
        return mergedList.next
    

def main():
    list1 = [ListNode(1), ListNode(2), ListNode(4)]
    list2 = [ListNode(1), ListNode(3), ListNode(4)]


    print(Solution().mergeTwoLists(list1, list2))


if __name__=='__main__':
    main()
