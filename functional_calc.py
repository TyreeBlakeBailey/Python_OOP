from Calculator import Calculator


class Functional_cacl(Calculator):

    def __init__(self):
        super().__init__()

    def percentage(Num1, Num2):  # Function that will work out the given percentage of a given number
        Answer = (Num1 / 100) * Num2
        return f"{Num1}% of {Num2} is {Answer}"  # returns the answer in this string format that can be printed

    def divisible(Num1, Num2):  # Function that will check if one give number is divisible by the other
        if Num2 == 0:  # Similar to the divide function you can not enter 0 as the second number
            raise ZeroDivisionError
        else:  # if the numbers entered are okay it will carry on with the maths process
            if Num1 % Num2 == 0:  # if a given number is divisble it will return the remainder (% find remainder) of 0
                return True  # if it is 0 it is divisible and will return True
            else:  # if teh remainder is another other then zero it will return False
                return False

    def triangle(Num1, Num2):  # Function to work out the area of a triangle
        if Num2 == 0 or Num1 == 0:  # Similar to the divide function you can not enter 0 as a length
            raise ZeroDivisionError
        else:  # As long as there is no errors or zeros given it will run the
            return f"The area of the triangle is {(Calculator.multiply(Num1, Num2)) / 2}"

    def inch_cm(Num1):  # function used to convert and given number of inches into cm
        return round(Calculator.multiply(Num1, 2.54), 5)
        # returns the answer of the conversion rate and rounds to the second decimal place
