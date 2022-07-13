n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    if i%2==0:
        s=s+a[i]
    if i%2!=0:
        c=c+a[i]
if s-c==0:
    print('YES')
else:
    print("NO")