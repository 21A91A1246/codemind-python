from collections import Counter
s=input()
k=Counter(s)
l=[]
f=0
for i,j in k.items():
    l.append(j)
l=set(l)
if len(l)<=1:
    print(-1)
else:
    l=sorted(l)[-2]
    for i in s:
        if s.count(i)==l and l>1:
            f=1
            print(i)
            break
    if f==0:
        print(-1)

    
        
        