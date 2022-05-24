def sd(n):
    t=n
    dc=0
    fc=0
    while(n):
        d=n%10
        dc+=1
        if(d!=0):
            if(t%d==0):
                fc+=1
        n=n//10
    if(dc==fc):
        return True
    else:
        False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if sd(i):
        print(i,end=' ')

