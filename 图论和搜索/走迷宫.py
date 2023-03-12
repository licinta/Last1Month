def maze_solve(n, m, maze):
    q = [[0, 0, 0]]
    v = [[1 for i in range(m)] for j in range(n)]
    v[0][0] = 0
    while True:
        cur = q.pop(0)
        curx, cury, curd = cur[0], cur[1], cur[2]
        if [curx, cury] == [n - 1, m - 1]:
            print(curd)
            return

        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y, d = curx + i, cury + j, curd + 1
            if 0 <= x < n and 0 <= y < m and v[x][y] and maze[x][y] == 0:
                v[x][y] = 0
                q.append([x, y, d])


n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))
maze_solve(n, m, maze)