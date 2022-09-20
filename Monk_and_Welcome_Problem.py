n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    c=a[i]+b[i]
    print(c,end=' ')
    