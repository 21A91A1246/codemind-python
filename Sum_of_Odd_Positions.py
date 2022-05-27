n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(n):
    if i%2!=0:
        s=s+a[i]
    #print(i,a[i])
print(s)
