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

while True:
    print("===Simple Calculator===")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n7. Exit")
    n=int(input("Enter Your Choice:"))
    if n==1:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(f"Addition of {a} and {b} is: {addition(a,b)}")

    elif n==2:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(f"Subtraction of {a} and {b} is: {subtraction(a,b)}")
    elif n==3:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(f"Multiplication of {a} and {b} is: {multiplication(a,b)}")   

    elif n==4:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(f"Division of {a} and {b} is: {division(a,b)}")

    elif n==5:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(f"Modulus of {a} and {b} is: {modulus(a,b)}")

    elif n==6:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(f"Exponentiation of {a} and {b} is: {exponentiation(a,b)}")   

    elif n==7:
        print("Thank You for using the calculator!")
        break
    else:
        print("Invalid Choice! Please try again.")