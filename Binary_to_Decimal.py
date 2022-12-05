def decimal(n):
    dec,i=0,0
    s=len(n)
    while i<len(n):
        dec+=int(n[s-1-i])*pow(2,i)
        i+=1
    return(dec)
for i in range(int(input())):
    a=input()
    print(decimal(a))
    
    