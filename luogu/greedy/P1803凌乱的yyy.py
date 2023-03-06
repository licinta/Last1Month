def SolutionP1803(n, start, end):
    li = list(zip(start, end))
    li.sort(key=lambda x: (x[1], x[0]))
    cnt, e = 0, 0
    for i, j in li:
        if cnt == 0:
            e = j
            cnt += 1
            continue
        if i >= e:
            cnt += 1
            e = j
    return cnt


n = int(input())
start, end = [], []
for i in range(n):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)
print(SolutionP1803(n, start, end))
