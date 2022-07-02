n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
min=0
k=0
for i in range(n):
    if a[i]>=x and a[i]<=y:
        k=1
        if a[i]>min:
            min=a[i]
if k==1:            
 print(min)
else:
    print('-1')