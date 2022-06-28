num = int(input())  
num_of_digits = len(str(num))  
sq= num*num 
end = sq%pow(10,num_of_digits)  
if end == num:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number")  