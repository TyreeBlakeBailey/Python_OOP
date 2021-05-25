import random
import math


# can also call "from random import random" that will allow you to only import teh funtion that you need
# print(random.random())
# # Will print out a random number
#
# num1 = 14.9
# print(num1)
# print(math.ceil(num1))  # will always round the given number up
# print(math.floor(num1))  # Will also round thd number down
# print(ran_num)

def round(Num):
    if math.modf(Num)[ 0 ] >= 0.50:
        return f"Number rounded up: {math.ceil(Num)}"
    elif math.modf(Num)[ 0 ] < 0.50:
        return f"Number rounded down: {math.floor(Num)}"


def IS_String(Input):
    try:
        Input = float(Input)
        if isinstance(Input, float):
            return True
        else:
            return False
    except ValueError:
        return False

while True:
    User_Num = input("Enter a decimal number to round\n")
    if IS_String(User_Num):
        print(round(float(User_Num)))
    else:
        print("Please enter correct value")
    print(f"The random generate number rounded is {round(random.random())}")
