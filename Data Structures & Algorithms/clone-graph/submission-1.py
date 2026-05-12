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

        def dfs(node):
            newnode = Node(node.val)
            visited[node] = newnode

            for neighbor in node.neighbors:
                if neighbor in visited:
                    newnode.neighbors.append(visited[neighbor])
                else:
                    newnode.neighbors.append(dfs(neighbor))

            return newnode

        if not node:
            return None

        return dfs(node)