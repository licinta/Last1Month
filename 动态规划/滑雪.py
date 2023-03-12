import functools
from sys import setrecursionlimit

setrecursionlimit(100005)
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))


def next_choice(i, j):
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + dx, j + dy
        if ni < 0 or nj >= m or ni >= n or nj < 0 or board[ni][nj] >= board[i][j]:
            continue
        yield ni, nj


@functools.lru_cache(None)
def dp(i, j):
    ans = 1
    for ni, nj in next_choice(i, j):
        ans = max(dp(ni, nj) + 1, ans)
    return ans


ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp(i, j))
print(ans)
