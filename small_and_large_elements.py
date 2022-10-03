s=input()
min=999
max=0
for i in s:
    if i==' ':
        break
    if min>ord(i):
        min=ord(i)
s=s[::-1]        
for i in s:
    if i==' ':
        break
    if max<ord(i):
        max=ord(i)
print(chr(min),chr(max),end=' ')        
    