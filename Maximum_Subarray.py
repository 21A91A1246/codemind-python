n=int(input())
x=list(map(int,input().split()))
a=x[0];b=x[0]
for i in range(1,n):
    b=max(x[i],b+x[i])
    a=max(b,a)
print(a)