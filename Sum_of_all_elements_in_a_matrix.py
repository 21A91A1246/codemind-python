a,b=map(int,input().split())
z=0
x=0
for i in range(a):
    s=list(map(int,input().split()))
    for i in s:
        z=z+i
print(z)