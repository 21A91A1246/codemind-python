n=int(input())
s=0
temp=n
if n<0:
    n=n*(-1)
while(n):
    r=n%10
    s=s*10+r
    n=n//10
if(temp<0):
    s=s*(-1)
    print(s)
else:
    print(s)
    