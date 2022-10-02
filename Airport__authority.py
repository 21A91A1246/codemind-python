n=int(input())
a=[]
s=0
for i in range(n):
    b=int(input())
    a.append(b)
t=int(input())
for i in range(n):
    if a[i]<=t:
        s=s+1
    else:
        s=s+2
print(s)        