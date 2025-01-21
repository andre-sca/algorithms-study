"""
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists.
The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


head = create_linked_list([1, 2, 3, 4])
print(hasCycle(head))

# Time: O(n)
# Space: O(1)
