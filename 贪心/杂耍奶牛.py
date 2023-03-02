n = int(input())
w, s = [], []
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    s.append(b)

cow = list(zip(w, s))
cow.sort(key=lambda x: x[0] + x[1])

# print(cow)
a = cow[0][0]
ans = -cow[0][1]
for i, j in cow[1:]:
    ans = max(ans, a - j)
    a += i
print(ans)
