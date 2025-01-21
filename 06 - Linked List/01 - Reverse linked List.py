"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
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


def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


input_list = [0, 1, 2, 3]
head = create_linked_list(input_list)
reversed_head = reverseListIterative(head)
print_linked_list(reversed_head)
# Time: O(n)
# Space: O(1)
