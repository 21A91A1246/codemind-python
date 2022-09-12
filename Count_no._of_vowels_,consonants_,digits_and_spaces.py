n=input()
a=0
b=0
c=0
d=0
for i in n:
    if i in 'aeiouAEIOU':
        a+=1
    if i not in 'aeiouAEIOU':
        b+=1
    if i in '0123456789':
        c+=1
    if i in " ":
        d+=1
print('Vowels:',a)
print('Consonants:',b-(c+d))
print('Digits:',c)
print('White spaces:',d)