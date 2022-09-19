n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i!=0:
        c.append(i)
#print(*c)
for i in a:
    if i==0:
        b.append(i)
d=c+b
print(*d)

        