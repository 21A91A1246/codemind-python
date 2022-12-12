n=int(input())
a=list(map(int,input().split()))
x=0
a=a[::-1]
for i in range(n):
    x+=a[i]*pow(2,i)
print(x)