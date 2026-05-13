class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def bfs(row, col):
            chain = []
            turntoX = True
            queue = deque([(row, col)])
            visited.add((row, col))

            directions = [[-1,0], [1,0], [0,1], [0,-1]]

            while queue:
                row, col = queue.popleft()
                chain.append((row, col))

                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    turntoX = False

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and board[nr][nc] == "O"
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            if turntoX:
                for row, col in chain:
                    board[row][col] = "X"

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in visited:
                    bfs(row, col)