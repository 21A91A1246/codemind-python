n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
k=0
for i in range(n):
    if a[i]>=x and a[i]<=y:
        b.append(a[i])
        #print(a[i])
print(sum(b))
        