n=int(input())
c=0
while n>5:
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    elif n%5==0:
        n=n//5
    else:
        c=1
        break
if c==1 or n<=0:
    print("Not Ugly Number")
else:
    print("Ugly Number")