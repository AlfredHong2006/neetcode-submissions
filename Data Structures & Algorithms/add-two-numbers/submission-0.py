# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        n2 = []
        while l1 is not None:
            n1.append(l1.val)
            l1=l1.next
        while l2 is not None:
            n2.append(l2.val)
            l2=l2.next
        n1.reverse()
        n2.reverse()

        n1_val = int("".join(map(str,n1)))
        n2_val = int("".join(map(str,n2)))
        ret = n1_val+n2_val
        ret = list(map(int,str(ret)))
        ret.reverse()
        
        tgt = ListNode(ret[0])
        copy = tgt
        
        for i in range(1,len(ret)):
            tgt.next = ListNode(ret[i])
            tgt = tgt.next
        
        return copy
        
        
