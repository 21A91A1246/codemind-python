s=input().split()
ms=0
mis=0
for i in s:
    x=[]
    for j in range(len(i)):
        x.append(ord(i[j]))
    m=max(x)
    mi=min(x)
    ms=ms+m
    mis=mis+mi
print(ms-mis)