n=int(input())
a=str(n)
b=list(a)
c=[]
for i in b:
    if i not in c:
        c.append(i)
if c==b:
    print("Unique Number")
else:
    print("Not Unique Number")