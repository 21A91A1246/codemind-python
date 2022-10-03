s=input()
s=s.lower()
s=s.split()
c=0
k=s[0]
for i in k:
    for j in s:
        if i in j:
            continue
        else:
            break
    else:
        c+=1
print(c)        
        
        