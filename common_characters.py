s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
c=''
for i in s1:
    if i in s2 and i!=' ':
        c+=i
c=set(c)
c=sorted(c)
s=''
f=0
for i in c:
    s+=i
    f=1
if f==0:
    print(-1)
else:
    print(s)
    