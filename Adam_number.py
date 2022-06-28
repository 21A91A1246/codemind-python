n=int(input())
a=n*n
s=0
s1=0
while(n):
    r=n%10
    s=s*10+r
    n//=10
b=s*s
while(b):
    r=b%10
    s1=s1*10+r
    b//=10
if s1==a:
    print(True)
else:
    print(False)