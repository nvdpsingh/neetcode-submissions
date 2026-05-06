class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        area = 0
        def bfs(r,c)->int:
            q = collections.deque()
            q.append((r, c))
            count = 1
            while q:
                r, c = q.popleft()
                grid[r][c]=0
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 0
                        q.append((row,col))
                        count+=1
            return count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    area = max(area,bfs(r,c))
        return area