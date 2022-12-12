def fun(l):
    s=[]
    for i in range(len(l)+1):
        for j in range(i):
            s.append(l[j:i])
    return(s)
a=int(input())
b=int(input())
#print(a,b)
l=[]
c=0
for i in range(a,b+1,1):
    l.append(i)
for i in fun(l):
    if sum(i)%2!=0:
        c+=1
print(c)