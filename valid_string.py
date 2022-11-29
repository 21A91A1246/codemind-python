s=input()
s=list(s)
l=s.count(min(s))
for i in s:
    if s.count(i)!=l:
        s.append(i)
        break
for i in s:
    if s.count(i)!=l:
        print("Not Valid")
        break
else:
    print("Valid String")
#print(s)
        
    
