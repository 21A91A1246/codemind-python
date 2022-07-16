n=int(input())
a=list(map(int,input().split()))
#print(a)
x,y=map(int,input().split())
#print(x,y)
k=0
max=0
for i in range(n):
    if a[i]<x or a[i]>y:
        k=1
        if a[i]>max:
            max=a[i]
        #break
if k==0:
    print(-1)
else:
    print(max)
        
        