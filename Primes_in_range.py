def isprime(k):
    if k==1:
        return False
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if(isprime(i)):
        c=c+1
print(c)