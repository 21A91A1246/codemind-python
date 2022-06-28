n=int(input())
s=0
a=n*n
while(a):
    r=a%10
    s=s+r
    a//=10
if(n==s):
    print('Neon Number')
else:
    print('Not Neon Number')