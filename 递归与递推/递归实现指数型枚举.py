a=int(input())

import random
import itertools
li=[i for i in range(1,a+1)]

ans=[]

for i in range(1,a+1):
    for j in itertools.combinations(li,i):
        ans.append(list(j))

print()
random.shuffle(ans)
for i in ans:
    print(*i)
