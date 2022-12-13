s=input()
s=s.lower()
s=s.split()
#print(s)
z=[]
for i in range(len(s)):
    #print(s[i])
    c=0
    for j in s[i]:
        if j in 'aeiou':
            c+=1
    z.append(c)
x=max(z)
print(z.count(x))