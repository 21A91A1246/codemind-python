n=int(input())
a=list(map(int,input().split()))
b=n//2
c=a[:b:1]
d=a[b::1]
print(sum(c))
print(sum(d))