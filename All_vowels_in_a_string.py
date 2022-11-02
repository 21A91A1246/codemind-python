s=input()
#s=s.lower()
s=set(s)
#print(s)
c=0
c1=0
for i in s:
    if i in "aeiou":
        c+=1
    elif i in "AEIOU":
        c1+=1

if c==5 or c1==5:
    print(True)
else:
    print(False)