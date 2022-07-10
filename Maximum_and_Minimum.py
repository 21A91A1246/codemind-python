n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
k=0
for i in a:
    b.append(a.count(i))
for i in range(n):
    if a[i]==b[i]:
        c.append(b[i])
    else:
        k+=1
if k!=n:        
 print(min(c),max(c))
else:
    print('-1') 