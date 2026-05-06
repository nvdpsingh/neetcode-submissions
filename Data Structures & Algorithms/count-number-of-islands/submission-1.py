class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows,cols = len(grid), len(grid[0])
        isIsland = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c = q.popleft()
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]=='1' and (row,col) not in visit:
                        q.append((row,col))
                        visit.add((row,col))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    isIsland+=1
        return isIsland      
        