n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
max=0
k=0
for i in range(n):
    if a[i]>=x and a[i]<=y:
        k=1
        if a[i]>max:
            max=a[i]
if k==1:
    print(max)
else:
    print('-1')
        
        
        
