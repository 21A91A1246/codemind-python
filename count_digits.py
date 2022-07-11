n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i<0:
        i=i*(-1)
    c=0
    if i==0:
        b.append(1)
        continue
    while(i):
        c+=1
        i//=10
    b.append(c)
print(*b)
    