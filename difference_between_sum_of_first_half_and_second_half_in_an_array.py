n=int(input())
a=list(map(int,input().split()))
b=n//2
c=a[:b:1]
d=a[b::1]
e=sum(c)-sum(d)
if e<0:
    e=e*(-1)
print(e)