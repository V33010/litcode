"""
LeetCode 0002: add two numbers
Difficulty: Medium
"""

import time
from copy import copy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(l):
    output = []
    while l:
        # print(l.val)
        output.append(l.val)
        l = l.next
    print(output)
    return 0


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        list1_pointer = l1
        list2_pointer = l2

        current = ListNode(0)
        carry = 0
        list_head = current

        while (list1_pointer) or (list2_pointer) or (carry != 0):

            val1 = list1_pointer.val if list1_pointer else 0
            val2 = list2_pointer.val if list2_pointer else 0
            total = val1 + val2 + carry

            units_val = total % 10
            carry_val = total // 10
            carry = carry_val

            current.next = ListNode(units_val)
            current = current.next

            if list1_pointer and list1_pointer.next:
                list1_pointer = list1_pointer.next
            else:
                list1_pointer = None

            if list2_pointer and list2_pointer.next:
                list2_pointer = list2_pointer.next
            else:
                list2_pointer = None

        return list_head.next


if __name__ == "__main__":
    # Utility functions
    def list_to_listnode(lst):
        head = ListNode(0)
        current = head
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return head.next

    def listnode_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Create Solution instance
    sol = Solution()

    # -------- Test Cases --------
    # Test case 1: 342 + 465 = 807
    l1 = list_to_listnode([2, 4, 3])
    l2 = list_to_listnode([5, 6, 4])
    res = sol.addTwoNumbers(l1, l2)
    assert listnode_to_list(res) == [7, 0, 8], "Test case 1 failed"

    # Test case 2: 0 + 0 = 0
    l1 = list_to_listnode([0])
    l2 = list_to_listnode([0])
    res = sol.addTwoNumbers(l1, l2)
    assert listnode_to_list(res) == [0], "Test case 2 failed"

    # Test case 3: 9999 + 1 = 10000
    l1 = list_to_listnode([9, 9, 9, 9])
    l2 = list_to_listnode([1])
    res = sol.addTwoNumbers(l1, l2)
    assert listnode_to_list(res) == [0, 0, 0, 0, 1], "Test case 3 failed"

    print("All local tests passed ✅")
