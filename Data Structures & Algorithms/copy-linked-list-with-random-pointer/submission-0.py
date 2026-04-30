class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hashmap = {}

        # First pass: create all nodes
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random
        curr = head
        while curr:
            if curr.next:
                hashmap[curr].next = hashmap[curr.next]
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]