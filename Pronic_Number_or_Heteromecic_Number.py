n=int(input())
m=0
for i in range(0,n):
    if i*(i+1)==n:
        m=1
        break
if(m==1):
    print('YES')
else:
    print('NO')
    
    