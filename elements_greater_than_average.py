n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
k=0

for i in range(n):
    if a[i]>=avg:
        
        k+=1
print(k)