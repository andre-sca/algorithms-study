"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
"""


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


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2

    return dummy.next


list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 5])
res = mergeTwoLists(list1, list2)
print_linked_list(res)

# Time: O(n + m)
# Space: O(1)
