# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        dummy = head
        nodelist = []

        while dummy:
            nodelist.append(dummy)
            dummy = dummy.next

        n = len(nodelist)
        l,r = 0, n-1
        while l < r:
        
            nodelist[l].next = nodelist[r]
            l += 1
            if l < r:
                nodelist[r].next = nodelist[l]
                r -= 1

    
        nodelist[l].next = None  
            
