n=int(input())
a=list(map(int,input().split()))
b=n//2
c=a[:b:1]
d=a[b::1]
e=sum(c)
d=sum(d)
res=e-d
if res<0:
    res=res*(-1)
print(res)