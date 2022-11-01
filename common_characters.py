a=input()
a=a.lower()
b=input()
b=b.lower()
k=0
c=[]
for i in a:
    if i in b:
        c.append(i)
c=set(c)
c=sorted(c)
z=''
for i in c:
    if i==' ':
        continue
    else:
        z+=(i)
        k=1
if k==0:
    print(-1)
else:
    print(z)