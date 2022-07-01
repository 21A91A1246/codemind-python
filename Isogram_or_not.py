a=input()
c=0
s=[]
for i in a:
    if i not in s:
        s.append(a.count(i))
for j in s:
    if j==2:
        print(False)
        break
else:
    print(True)
