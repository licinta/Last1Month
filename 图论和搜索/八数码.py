li = input().split()

s = set()
from collections import deque


def func(seq):
    q = deque([[seq, 0]])
    while q:
        cur, step = q.popleft()
        if cur == '12345678x':
            return step
        li = list(cur)
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            x = cur.index('x')
            x, y = x // 3, x % 3
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 3 and 0 <= ny < 3):
                continue
            li[x * 3 + y], li[nx * 3 + ny] = li[nx * 3 + ny], li[x * 3 + y]
            nes = ''.join(li)
            if nes not in s:
                s.add(nes)
                q.append([nes, step + 1])
            li[x * 3 + y], li[nx * 3 + ny] = li[nx * 3 + ny], li[x * 3 + y]
    return -1


print(func(''.join(li)))
