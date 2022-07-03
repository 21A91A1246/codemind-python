def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in range(n):
    if a[i]==1:
        continue
    if prime(a[i]):
        b.append(a[i])
res=(sum(b)/len(b))
print('{:.2f}'.format(res))