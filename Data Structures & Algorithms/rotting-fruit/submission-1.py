class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        def bfs(queue: deque) -> int:
            minutes = 0
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:
                inc = 0

                for _ in range(len(queue)):  # one full minute
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue

                        if grid[nr][nc] != 1:
                            continue

                        grid[nr][nc] = 2
                        inc = 1
                        queue.append((nr, nc))

                if inc == 1:
                    minutes += 1

            return minutes

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        answer = bfs(queue)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return answer






