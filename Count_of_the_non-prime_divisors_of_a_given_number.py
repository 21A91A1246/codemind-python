def prime(a):
    for i in range(2,a):
        if a%i==0:
            return 1
    else:
        return 0
n=int(input())
c=1
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            c+=1
print(c)