import math
import random
import datetime

def square_root(num):
    print(math.sqrt(num))

def random_number():
    print(random.randint(1, 100))

def current():
    print(datetime.datetime.now())

print("===Math Operations===")
n=int(input("Enter a number:"))
square_root(n)
print("===Random Number===")
random_number()
print("===Current Date and Time===")
current()
