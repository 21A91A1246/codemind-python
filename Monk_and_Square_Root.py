t=int(input())
for i in range(t):
    f=0
    a,b=map(int,input().split())
    for i in range(0,b):
        if (i*i)%b==a:
            f=1
            print(i)
            break
    if f==0:
        print(-1)
#(x*2)%m=n
#(n*m)%2=x