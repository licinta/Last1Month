s,t=map(int,input().split())

n=int(input())

li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append([a,b])

li.sort()

cnt,i=0,0
while i<len(li):
    temp=s
    cnt+=1
    if li[i][0]>temp:break
    while i<len(li) and li[i][0]<=temp:
        s=max(s,li[i][1])
        # print("*****",li[i])
        i+=1
    if s>=t:
        break
if s>=t:
    print(cnt)
else:
    print(-1)

