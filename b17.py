num1 = int(input("Enter a number: "))  
sum = 0  
temp = num1  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num1 == sum:  
   print("yes")
else:
   print("no")
