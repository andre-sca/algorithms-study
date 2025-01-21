"""
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
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


def removeNthFromEndMine(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    i = 0
    dummy = aux = ListNode()
    while i < n:
        aux.next = head
        head = head.next
        aux = aux.next
        i += 1
    if not head:
        return None
    aux.next = head.next
    return dummy.next


head = create_linked_list([1, 2, 3, 4])
res = removeNthFromEndMine(head, 2)
print_linked_list(res)
head2 = create_linked_list([5, 3])
res2 = removeNthFromEndMine(head2, 1)
print_linked_list(res2)


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


head = create_linked_list([1, 2, 3, 4])
res = removeNthFromEnd(head, 2)
