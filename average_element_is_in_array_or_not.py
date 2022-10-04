a=int(input())
z=list(map(int,input().split()))
x=sum(z)//a
for i in z:
    if i==x:
        print(True)
        break
else:
    print(False)