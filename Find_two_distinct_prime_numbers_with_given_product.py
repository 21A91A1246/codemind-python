def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
k=0
for i in range(2,(n//2)+1):
    if prime(i):
        for j in range(i+1,(n//2)+1):
            if prime(j):
                if i*j==n:
                    k=1
                    print(i,j)
                    break
    if k==1:
        break
else:
    print("-1")