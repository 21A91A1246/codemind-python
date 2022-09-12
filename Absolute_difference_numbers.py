a,b=map(str,input().split())

#print(a,b)
d=int(b)
c=a[:d:]
s=a[::-1]
x=s[:d:]
f=x[::-1]

z=(int(f)-int(c))
if (z<0):
    z=z*(-1)
print(z)
