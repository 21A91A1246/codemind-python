n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
k=0
l=[]
for i in range(n):
    if a[i]>=b and a[i]<=c:
        k=1
        l.append(a[i])
if k==0:
    print(-1)
else:
    print(*l)