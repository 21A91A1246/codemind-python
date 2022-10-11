n=int(input())
for i in range(n):
    a=int(input())
    z=input()
    #print(z)
    for i in range(a):
        if z.count(z[i])==1:
            print(z[i])
            break
    else:
        print(-1)