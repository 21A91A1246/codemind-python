n=int(input())
a=list(map(int,input().split()))
b=[]
s=[]
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
for i in range(len(b)):
    if b[i]%2==0:
        s.append(b[i])
print(len(s))