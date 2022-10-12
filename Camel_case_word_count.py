a=input()
c=0
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in a:
    if i in s:
        c+=1
if a[0] not in s:
    c+=1
print(c)