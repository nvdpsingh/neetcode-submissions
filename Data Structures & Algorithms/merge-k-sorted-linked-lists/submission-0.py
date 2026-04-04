import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []          # min‑heap of (val, index, node)
        dummy = ListNode(0)
        curr = dummy

        # push all non‑empty heads
        index = 0
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, index, node))
                index += 1

        while h:
            val, idx, node = heapq.heappop(h)
            curr.next = node
            curr = curr.next

            if node.next:
                index += 1
                heapq.heappush(h, (node.next.val, index, node.next))

        return dummy.next