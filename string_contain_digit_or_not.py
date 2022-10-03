n=input()
c=0
for i in n:
    if i.isdigit():
        c+=1
if c>=1:
    print('Contains',c, "digit")
else:
    print("Doesn't contain digit")