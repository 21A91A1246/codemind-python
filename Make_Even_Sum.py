n=int(input())
a=list(map(int,input().split()))
#from itertools import combinations
x=[]
#k=combinations(a,2)
f=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if (a[i]+a[j])%2!=0:
            f=1
            break
        else:
            f=0
if f==0:
    print("1")
else:
    print("0")