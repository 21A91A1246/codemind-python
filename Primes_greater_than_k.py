def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=0
b=[]
for i in range(n):
    if a[i]>=x:
        b.append(a[i])
for i in range(len(b)):
    if b[i]==1:
        continue
    if prime(b[i]):
        c+=1
print(c)
