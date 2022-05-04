n=int(input())
len_num=len(str(n))
sq=n*n
ld=sq%pow(10,len_num)
if(ld==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')