n=int(input())
for i in range(n): #0,1
    a=int(input())
    temp=a
    s=0
    while(temp):
        r=temp%10
        s=s*10+r
        temp=temp//10
    if(s==a):
        print('True')
    else:
        print('False')
    