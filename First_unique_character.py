s=input()
s=s.lower()
a=[]
b=0
for i in range(len(s)):
    
    if s.count(s[i])==1:
        a.append(s[i])
        b=1
        break
if b==0:
    print(-1)
else:
    print(*a)