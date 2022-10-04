b=int(input())
z=list(map(int,input().split()))
#x=int(input())
for i in range(b):
    if z[i]%2==0:
        c=i
print(c)