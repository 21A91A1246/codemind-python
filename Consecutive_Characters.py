a=input()
b=set(a)
c=0

p=[]
for i in b:
    maxi=0
    for j in range(len(a)):
        if i==a[j]:
            c+=1
            maxi=max(c,maxi)
        else:
            c=0
    p.append(maxi)
print(max(p))