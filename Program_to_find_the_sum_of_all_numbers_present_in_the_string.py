n=input()
new=[]
sum=0
for i in n:
    if i.isdigit():
        new.append(int(i))
for j in new:
    sum=sum+j
print(sum)

