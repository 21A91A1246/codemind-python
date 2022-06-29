n=int(input())
a=[]
while n:
    d=n%10
    a.append(d)
    n//=10
a=a[::-1]
for i in range(len(a)):
    if a[i]==6:
        a[i]=9
        break
r=0    
for i in range(len(a)):
   r=r*10+a[i]
print(r)   
    