n=int(input())
s=0
t=n
while(n):
    r=n%10
    s=s*10+r
    n//=10
if t==s:
    print(True)
else:
    print(False)