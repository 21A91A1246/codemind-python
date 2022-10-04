s=input()
s=s.lower()
a=[]
b=[]
for i in range(len(s)):
    if s[i]==' ':
        continue
    if s.count(s[i])==1:
        a.append(s[i])
b=sorted(a)
for i in b:
    print(i,end='')