def for_loop(n):
    for i in range(1,n+1):
        print(i)

def while_loop(n):
    i=1
    while i<=n:
        print(i)
        i+=1

def multiplication(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")


print("===For Loop===")
n=int(input("Enter a number:")) 
for_loop(n)

print("===While Loop===")
n=int(input("Enter a number:"))
while_loop(n)

print("===Multiplication Table===")
n=int(input("Enter a number:"))
multiplication(n)