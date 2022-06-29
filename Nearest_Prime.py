a=int(input())
for p in range(a):
 k=int(input())
 for i in range(k,2,-1):
    for j in range(2,i):
     if i%j==0:
      #print(i)
      break
    else:
      break
 for m in range(k+1,k+100):
    for n in range(2,m):
     if m%n==0:
      #print(i)
      break
    else:
      break 
 if abs(k-m)>=abs(k-i):
     print(i)
 else:
     print(m)