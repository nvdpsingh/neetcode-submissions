class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows,cols = len(grid), len(grid[0])
        count = 0
        def bfs(start:tuple[int],visited:set()):
            if grid[start[0]][start[1]] == '0' or (start[0],start[1]) in visited:
                return 0
            queue = deque([start])
            visited.add(start)
            while queue:
                (r,c) = queue.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1" and (nr,nc) not in visited):
                        queue.append((nr,nc))
                        visited.add((nr,nc))                      
            return 1
        
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited:
                    count+= bfs((row,col),visited)
        return count
                