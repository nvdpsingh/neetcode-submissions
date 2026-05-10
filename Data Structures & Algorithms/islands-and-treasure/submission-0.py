class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        def bfs(queue : deque):
            while queue:
                (r,c) = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr<0 or nr>=rows or nc<0 or nc>=cols:
                        continue
                    
                    if grid[nr][nc]!= INF:
                        continue
                    
                    grid[nr][nc] = grid[r][c]+1
                    queue.append((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c))
        bfs(queue)
                