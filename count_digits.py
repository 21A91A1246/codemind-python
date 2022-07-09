def fun(n):
    c=0
    if(n<0):
        n=n*(-1)
    while(n):
        r=n%10
        c+=1
        n//=10
    return c
a=int,input()
x=list(map(int,input().split()))
#print(x)
f=[]
#print(x)
for i in x:
   if i==0:
       print('1',end=' ')
       continue
   print(fun(i),end=' ')