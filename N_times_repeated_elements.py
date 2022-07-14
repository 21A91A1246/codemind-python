n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=[]
f=0
for i in range(n):
    if a.count(a[i])==k and a[i] not in c:
        c.append(a[i])
        f=1
if f==0:
    print(-1)
else:    
    print(*c)
 
 