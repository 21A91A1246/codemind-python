x=input()
a=len(x)
s=0
for i in range(0,a):
  k=0
  if(x[i]>='0' and x[i]<='9'):
     k=ord(x[i])
     s=s+k
     s=s-48
print(s)