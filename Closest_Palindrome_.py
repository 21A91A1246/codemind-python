def pal(n):
    a=n
    r=0
    while a:
        d=a%10
        r=r*10+d
        a//=10
    if r==n:
        return n
    else:
       return 0
n=int(input())
for i in range(n-1,1,-1):
    if pal(i):
        k=i
        break
for m in range(n+1,n+1000):
    if pal(m):
        j=m
        break
if abs(k-n)==abs(j-n):
    print(k,j)
elif abs(k-n)<abs(j-n):
    print(k)
else:
    print(j)