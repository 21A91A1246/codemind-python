n=int(input())
a=list(map(int,input().split()))
#print(a)
for i in a:
    b=a.count(i)
    if b>n//2:
        print(i)
        break
#print(b)