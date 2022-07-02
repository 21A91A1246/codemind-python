n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
k=0
for i in range(n):
    if a[i]<x or a[i]>y:
        k=1
        b.append(a[i])
if k==1:
   print(max(b))
else:
    print('-1')


        