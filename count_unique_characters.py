s=input()
s=s.lower()
a=[]
for i in range(len(s)):
    if s[i]==' ':
        continue
    if s.count(s[i])==1:
        a.append(s[i])
print(len(a))