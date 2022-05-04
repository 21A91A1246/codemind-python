a,b=map(int,input().split())
if(a>b):
    g=a
else:
    g=b
while(True):
    if(g%a==0 and g%b==0):
        print("%d"%g)
        break
    g+=1