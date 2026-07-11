# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a placeholder dummy node
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Connect the remaining portion of the non-empty list
        tail.next = list1 if list1 else list2
        
        # Return the actual sorted head
        return dummy.next
