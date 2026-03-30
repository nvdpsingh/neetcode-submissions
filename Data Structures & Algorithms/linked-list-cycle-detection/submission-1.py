# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = head
        seen = set()
        while dummy:
            if dummy in seen:
                return True
            else:
                seen.add(dummy)
                dummy = dummy.next
        return False