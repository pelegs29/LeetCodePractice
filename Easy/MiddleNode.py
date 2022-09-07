# 876. Middle of the Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head: ListNode) -> ListNode:
    if head is None:
        return head
    middle = head
    while True:
        if head.next is None:
            break
        head = head.next
        if head.next is None:
            middle = middle.next
            break
        head = head.next
        middle = middle.next
    return middle
