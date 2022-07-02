n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
c=[]
for i in range(len(b)):
    if b[i]%2!=0:
        c.append(b[i])
print(sum(c))

    