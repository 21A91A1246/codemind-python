n=int(input())
s=0
m=1
while(n):
    r=n%10
    s=s+r
    m=m*r
    n//=10
if(s==m):
    print('Spy Number')
else:
    print('Not Spy Number')