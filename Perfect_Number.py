n=int(input())
a=n
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==a:
    print(True)
else:
    print(False)
