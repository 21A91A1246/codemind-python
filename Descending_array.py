n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(a[i])

c=b[::-1]
a.sort()
#print(c)
#print(a)
if c==a:
    print('yes')
else:
    print('no')




