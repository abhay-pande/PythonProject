num= int(input("Enter a number: "))

def factorial( num):
 if (num <2):
     return 1
 else:
     return num * (factorial(num-1))

result=factorial(num)
print( "Factorial of "+ str(num) + " is: "+ str(result))