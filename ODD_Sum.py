n=int(input())
s=0
a=list(map(int,input().split()))
#print(a)
for i in range(n):
    if a[i]%2!=0:
        s=s+a[i]
print(s)
        