# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find the midpoint first
        slow, fast = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            #this finds the middle value


        forward = slow.next
        slow.next = None
        backwards = None

        while forward != None:
            tmp = forward.next
            forward.next = backwards
            backwards = forward
            forward = tmp
        
        slow_ptr = head

        while backwards != None:
            tmp = slow_ptr.next
            tmp2 = backwards.next
            slow_ptr.next = backwards
            backwards.next = tmp
            slow_ptr = tmp
            backwards = tmp2