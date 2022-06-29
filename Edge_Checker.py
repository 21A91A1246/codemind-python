a,b=map(int,input().split())
if a>b:
    a,b=b,a
if a==1:
    if b==10 or b==2:
        print("Yes")
    else:
        print("No")
elif b==10:
    if a==1 or a==9:
        print("Yes")
    else:
        print("No")
elif b==a+1 or b==a-1:
    print("Yes")
else:
    print("No")