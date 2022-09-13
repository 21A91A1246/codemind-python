n=int(input())
#print(n)
i=0
a=0
b=1
z=[]
while(i<=n//2):
    if(i<=1):
        nxt=i
    else:
        nxt=a+b
        a=b
        b=nxt
        z.append(nxt)
    #print(nxt)
    i+=1
for i in z:
    if n in z:
        print(True)
        break
    else:
        print(False)
        break