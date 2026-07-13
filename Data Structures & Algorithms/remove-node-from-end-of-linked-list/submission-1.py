# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        
        #reverse
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #take out nth node from the start
        head = prev

        if n == 1:
            head = head.next

        else:
            for _ in range(n - 2):
                prev = prev.next
            
            prev.next = prev.next.next
        
        #reverse back
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

        