n=int(input())
a=list(map(int,input().split()))
z=int(input())
for i in range(z):
    c=a.pop()
    a.insert(0,c)
print(*a)