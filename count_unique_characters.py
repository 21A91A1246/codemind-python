s=input()
s=s.lower()
x=[]
for i in s:
    if i==' ':
        continue
    else:
        x.append(s.count(i))
print(x.count(1))