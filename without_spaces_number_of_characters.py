a=input()
b=(len(a))
c=0
for i in a:
    if i in ' ':
        c+=1
print(b-c)