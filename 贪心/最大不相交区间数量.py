n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

p.sort()

# print(p)
cnt = 1
i, j = p[0]
for x, y in p[1:]:
    i = max(i, x)
    j = min(j, y)
    if i > j:
        i, j = x, y
        cnt += 1


print(cnt)
