a=input()
b=[]
s=0
for i in a:
    if i in "aeiouAEIOU":
        b.append(i)
b=b[::-1]
#print(b)
for i in a:
    if i not in "aeiouAEIOU":
        print(i,end='')
    else:
        print(b[s],end='')
        s+=1
        