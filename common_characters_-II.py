s1=input()
s1=s1.lower()
s1=set(s1)
s2=input()
s2=s2.lower()
s2=set(s2)

c=0
for i in s1:
    if i in s2 and i!=' ':
        c+=1
print(c)