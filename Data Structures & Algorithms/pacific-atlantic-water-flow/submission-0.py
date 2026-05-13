class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        results = []

        def bfs(row, col):
            atlantic, pacific = False, False
            queue = deque([(row, col)])
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            visited = set([(row, col)])
            
            while queue:
                row, col = queue.popleft()

                if row == 0 or col == 0:
                    pacific = True
                if row == rows - 1 or col == cols - 1:
                    atlantic = True

                if pacific and atlantic:
                    return True

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if (nr, nc) in visited:
                        continue

                    if heights[nr][nc] > heights[row][col]:
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))

            return pacific and atlantic

        for row in range(rows):
            for col in range(cols):
                if bfs(row, col):
                    results.append([row, col])

        return results