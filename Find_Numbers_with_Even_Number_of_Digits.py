def fun(n):
    c=0
    while(n):
        r=n%10
        c+=1
        n//=10
    return c
s=int(input())
a=list(map(int,input().split()))
b=0
for i in range(s):
    d=fun(a[i])
    if d%2==0:
        
        b+=1
print(b)