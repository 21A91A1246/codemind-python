a,b=map(int,input().split())
if a>b:
    ma=a
else:
    ma=b
while(True):
    if((ma%a==0) and (ma%b==0)):
        lcm=ma
        break
    ma+=1
print(ma)