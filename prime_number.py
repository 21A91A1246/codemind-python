def prime(s):
    for i in range(2,s//2):
        if s%i==0:
            return 0
    else:
        return 1
b=int(input())
if prime(b):
    print("prime")
else:
    print("not a prime")