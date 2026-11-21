# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #iterate through the head
        # i, ptr val
        i= 0
        kp = {}
        #use a dictionary with key value pairs
        #as soon as you hit the end of the list, return n
        #actually we need to "remove" the node.
        # curr = head
        # while curr != None:
        #     kp[i] = curr
        #     i += 1
        #     curr = curr.next
        # if n==1:
        #     if len(kp)== 1:
        #         head = head.next
        #     else:
        #         kp[i-2].next=None
        # elif (i-n)!=0:
        #     ptr_keep = kp[i-n-1]
        #     ptr_keep.next = kp[i-n+1]

        # else:
        #     head=head.next

        # return head

        dummy = ListNode (0,head)
        fast = dummy
        slow = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next