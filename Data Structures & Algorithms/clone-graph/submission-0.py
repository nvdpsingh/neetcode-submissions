"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited = {}
        
        
        
        def bfs(newnode: Node, node: Node,visited:dict):
            newnode = Node(node.val)
            visited[node] = newnode
            for neighbor in node.neighbors:
                if neighbor in visited:
                    newnode.neighbors.append(visited[neighbor]) # adding from visited to newnode's neighbors
                else:
                    newnode.neighbors.append(bfs(Node(),neighbor,visited))
            return newnode


        if not node:
            return None
        if not node.neighbors:
            return bfs(Node(),node,visited)
        return bfs(Node(),node,visited)