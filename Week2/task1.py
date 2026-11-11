def grade(n):
    if n>=50:
        if n>=90 and n<=100:
            print("A+")

        elif n>=80 and n<90:
            print("A")
        elif n>=70 and n<80:
            print("B")
        elif n>=60 and n<70:
            print("C")
        else:
            print("D")
    else:
        print("Fail")

print("===Grade Calculator===")
n=int(input("Enter Your mark:"))
grade(n)