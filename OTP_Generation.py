n=int(input())
s=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
x=s
while(x):
    r1=x%10
    if(r1%2!=0):
        sq=r1*r1
        print(sq,end='')
    x=x//10
    