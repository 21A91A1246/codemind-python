s=int(input())
c=0
while s>5:
    if s%2==0:
        s=s//2
    elif s%3==0:
        s=s//3
    elif s%5==0:
        s=s//5
    else:
        c=1
        break
if c==1 or s<=0:
    print("Not Ugly Number")
else:
    print("Ugly Number")