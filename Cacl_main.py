from Calculator import Calculator
from functional_calc import Functional_cacl


class Calc_Main(Functional_cacl):
    def __init__(self):
        super().__init__()

    def Start_Program(self):  # Function that will run to start the entire program to run (User interface)
        while True:  # continously run the following block of code until a break command is given
            try:  # Will run this block of code and if any error is raised anywhere it will skip to the expect section
                # at the bottom of the code instead of crashing teh program
                Input_Choice = input(
                    "\nPlease choose from the following....\nAdd, Subtract, Multiply, Divide, Percentage, Divisible, "
                    "Triangle, Inchtocm, Exit\n").capitalize()
                # User menu with capitalize to make sure it matches easily error check what ever the user enters from
                # the menu it will ask for one or two numbers and call the corresponding function entering the given
                # user numbers
                if Input_Choice == "Add":
                    Num1, Num2 = Calculator.Nums()
                    print(Calculator.add(Num1, Num2))
                elif Input_Choice == "Subtract":
                    Num1, Num2 = Calculator.Nums()
                    print(Calculator.subtract(Num1, Num2))
                elif Input_Choice == "Multiply":
                    Num1, Num2 = Calculator.Nums()
                    print(Calculator.multiply(Num1, Num2))
                elif Input_Choice == "Divide":
                    Num1, Num2 = Calculator.Nums()
                    print(Calculator.divide(Num1, Num2))
                elif Input_Choice == "Percentage":
                    print("Num1% of Num2 is Answer")
                    Num1, Num2 = Functional_cacl.Nums()
                    print(Functional_cacl.percentage(Num1, Num2))
                elif Input_Choice == "Triangle":
                    print("Enter base and height of the triangle")
                    Num1, Num2 = Calculator.Nums()
                    print(Functional_cacl.triangle(Num1, Num2))
                elif Input_Choice == "Divisible":
                    print("Enter bigger number first")
                    Num1, Num2 = Calculator.Nums()
                    if Functional_cacl.divisible(Num1, Num2):
                        print(f"{Num1} is divisible by {Num2}")
                    else:
                        print(f"{Num1} is not divisible by {Num2}")
                elif Input_Choice == "Inchtocm":
                    Inches = input('Enter inches to convert to cm ')
                    if Inches.isdigit():
                        print(f"{Functional_cacl.inch_cm(int(Inches))}cm")
                    else:
                        print("Invalid entry, try again")
                        continue
                elif Input_Choice == "Exit":  # The user can break the loop and exit by typing exit
                    break
                else:  # if the user doesn't enter a valid selection from the given menu it will print the following
                    # and loop again
                    print("Please enter valid method")

            except ZeroDivisionError:  # When Zero Division error is raised in the try method block of code it will
                # run the following line
                print("(‡ಠ╭╮ಠ) \nYou cannot use zero here ")
                continue  # continue will make sure the loop carries on even if an error is thrown
            except ValueError:  # When Value error is raised in the try method block of code it will
                # run the following line
                continue


Calc_Main().Start_Program()
