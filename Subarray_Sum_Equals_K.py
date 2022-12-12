def fun(l):
    z=[]
    for i in range(len(l)+1):
        for j in range(i):
            z.append(l[j:i])
    return(z)
a,b=map(int,input().split())
s=list(map(int,input().split()))
a=fun(s)
c=0
for i in a:
    if sum(i)==b:
        c+=1
print(c)