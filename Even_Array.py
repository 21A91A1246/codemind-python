n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(n):
    if a[i]%2!=0:
       k=1
if k==1:
    print(False)
else:
    print(True)