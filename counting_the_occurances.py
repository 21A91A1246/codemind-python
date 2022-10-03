b=input()
s=input()
c=0
for i in b:
    if s==i:
        c+=1
if c==0:
    print(-1)
else:
    print(c)
