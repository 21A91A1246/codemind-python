a=int(input())
c=0
for i in range(2,a):
    if a%i==0:
     print("Not Mega Prime")
     break
else:
    while a:
     d=a%10
     if d==1:
      c=1
      break
     for i in range(2,d):
      if d%i==0:
       c=1
       break
     a=a//10
    if c!=1:
      print("Mega Prime")
    else:
     print("Not Mega Prime")
      