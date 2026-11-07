def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b      
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b  
def modulus(a,b):
    return a%b  
def exponentiation(a,b):
    return a**b

n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
print(f"Addition of {n} and {m} is: {addition(n,m)}")
print(f"Subtraction of {n} and {m} is: {subtraction(n,m)}")
print(f"Multiplication of {n} and {m} is: {multiplication(n,m)}")
print(f"Division of {n} and {m} is: {division(n,m)}")
print(f"Modulus of {n} and {m} is: {modulus(n,m)}")
print(f"Exponentiation of {n} and {m} is: {exponentiation(n,m)}")