n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(n):
    if a[i] not in b:
        b.append(a[i])
for i in range(len(b)):
    if b[i]%2!=0:
        c+=1
print(c)