n=int(input())
a=list(map(int,input().split()))
c=n//2
b=a[:c:1]
d=a[c::1]
print(sum(b))
print(sum(d))
    