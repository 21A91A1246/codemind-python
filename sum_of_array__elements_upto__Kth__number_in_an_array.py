n=input()
a=list(map(int,input().split()))
m=int(input())
m=a.index(m)
s=0
for i in range(m+1):
    s=s+a[i]
print(s)    