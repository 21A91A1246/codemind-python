a=int(input())
z=list(map(int,input().split()))
x=int(input())
c=0
for i in z:
    if i==x:
        c+=1
print(c)