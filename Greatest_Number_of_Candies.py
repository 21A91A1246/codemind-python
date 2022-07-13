n=int(input())
a=list(map(int,input().split()))
#print(a,end=' ')
b=int(input())
c=max(a)
#print(c)
d=0
for i in range(n):
    k=a[i]+b
    if k>=c:
        print(True,end=' ')
    else:
        print(False,end=' ')