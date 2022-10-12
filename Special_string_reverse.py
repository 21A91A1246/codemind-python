s=input()
l=list(s)
res=[]
ind=[]
char=[]
for i in range(len(l)):
    if l[i].isalpha():
        res.append(l[i])
    else:
        char.append(l[i])
        ind.append(i)
res=res[::-1]
for i in range(len(ind)):
    res.insert(ind[i],char[i])
print(*res,sep='')