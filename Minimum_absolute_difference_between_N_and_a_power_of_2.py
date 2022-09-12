n=int(input())
for i in range(1,n):
    if 2**i > n:
        k=i
        break
if abs((2**(k-1))-n)<abs((2**k)-n):
    print(abs((2**(k-1))-n))
else:
    print(abs((2**k)-n))
        