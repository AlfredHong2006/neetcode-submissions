"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #task - create a deep copy.
        if head == None:
            return None
        
        old2new = {None: None}

        curr = head
        while curr is not None:
            old2new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr is not None:
            copy = old2new[curr]
            copy.next = old2new[curr.next]
            copy.random = old2new[curr.random]
            curr = curr.next
        return old2new[head]
        