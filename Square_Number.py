n=int(input())
for i in range(1,(n//2)+1):
    s=i*i
    if s==n:
      print(True)
      break
else:
    print(False)