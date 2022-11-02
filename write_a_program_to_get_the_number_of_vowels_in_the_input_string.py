s=input()
c=0
for i in s:
    if i in 'aeiouAEIOU':
        c+=1
if c==0:
    print(0)
else:
    print(c)