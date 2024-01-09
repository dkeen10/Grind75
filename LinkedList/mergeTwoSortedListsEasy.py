# https://leetcode.com/problems/merge-two-sorted-lists/


# given
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# created LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        # mergedList = []
        # m = len(list1)
        # n = len(list2)
        # i = 0
        # j = 0
        # while list1 or list2:
        #     if list1[i] >= list2[j]:
        #         mergedList.append(list1.pop())
        #         i = i + 1
        #     else:
        #         if list1[i] < list2[j]:
        #             mergedList.append(list2.pop())
        #             j = j + 1
        # return mergedList

        """
        Time complexity: O(n) since each element gets looked at once.
        """
        # create new LinkedList
        mergedList = LinkedList()

        # create pointers to iterate through lists
        pointer1 = list1
        pointer2 = list2

        # iterate through both lists
        while pointer1 and pointer2:
            # compare values of pointers
            if pointer1.val < pointer2.val:
                mergedList.append(pointer1.val)
                pointer1 = pointer1.next
            else:
                mergedList.append(pointer2.val)
                pointer2 = pointer2.next

        # add remaining nodes
        while pointer1:
            mergedList.append(pointer1.val)
            pointer1 = pointer1.next

        while pointer2:
            mergedList.append(pointer2.val)
            pointer2 = pointer2.next

        return mergedList


def main():
    list1 = ListNode 
    list2 = ListNode
    print(Solution().mergeTwoLists(list1, list2))


if __name__=='__main__':
    main()
