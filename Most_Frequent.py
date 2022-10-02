n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
d=[]
#print(a)
for i in range(n):
    d.append(a.count(a[i]))
x=d.index(max(d))
print(a[x])

