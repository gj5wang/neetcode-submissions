# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head

        #check if this current node is in set, if yes return true, if no move on to next
        #if a node is none return false
        while current:
            if current in visited:
                return True
            else:
                visited.add(current)
                nxt = current.next
                current = nxt
        return False
                
        