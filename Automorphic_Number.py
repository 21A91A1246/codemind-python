n=int(input())
l=len(str(n))
sq=n*n
a=pow(10,l)
ld=sq%a
if(n==ld):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
