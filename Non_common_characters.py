a=input()
b=input()
a=a.lower()
b=b.lower()
c=[]
for i in a:
    if i not in b and i!=' ':
        c.append(i)
for j in b:
    if j not in a and i!=' ':
        c.append(j)
c=set(c)
if(len(c)>0):
    print(len(c))