n=int(input())
c=0
for i in range(1,n):
    if(n==i*(i+1)):
        c=c+1
if c==1:
    print('YES')
else:
    print('NO')
        


    