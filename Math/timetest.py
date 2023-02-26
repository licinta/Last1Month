import time 
li=[]
begin=time.time()
for i in range(1000000):
    li.append(i)
end=time.time() 
print(li.append.__str__ ,'costs',end-begin)


li=[]
liappend=li.append
begin=time.time()
for i in range(1000000):
    liappend(i)
end=time.time() 
print(liappend.__str__ ,'costs',end-begin)
