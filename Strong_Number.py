n=int(input())
k=0
p=n
while(n):
    d=n%10
    s=1
    for i in range(1,d+1):
     s=s*i
    k=k+s 
    n=n//10
if k==p:
    print("The number",p,"is a strong number")
else:
     print("The number",p,"is not a strong number")
    