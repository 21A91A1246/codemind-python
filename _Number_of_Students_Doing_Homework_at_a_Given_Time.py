n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
q=int(input())
c=0
for i in range(n):
    if b[i]>=q and a[i]<=q:
        c+=1
print(c)