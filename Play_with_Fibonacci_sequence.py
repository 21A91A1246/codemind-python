n=int(input())
i=0
a=0
b=1
while(i<n):
    if(i<=1):
        nxt=i
    else:
        nxt=a+b
        a=b
        b=nxt
    print(nxt,end=' ')
    i+=1