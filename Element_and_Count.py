n=int(input())
a=list(map(int,input().split()))
c=[]
b=[]
for i in range(n):
   if a[i] in b:
       continue
   b.append(a[i])
   c.append(a[i]) 
   c.append(a.count(a[i]))
print(*c)   
   
   
    