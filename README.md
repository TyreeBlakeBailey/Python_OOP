# Python Object oriented programming

- Classes
- Python Packages
- Python Modules
- Pip
- API with requests

## The four pillars of object-oriented programming are:

### Abstraction
  - Hide away the implementation details inside something i.e a prototype, or a function 
  - When you are calling a function you don't need to know exactly what it is doing 

### Inheritance
  - Lets one object acquire the properties and method of another object
  - Allows for re-usability
    
### Encapsulation
  - Removing access to part of your code and making things private
  -  Encapsulation means that each object in your code should control its own state.
  - Example below of how to create a private variable or modules 
- Can only be called from within its own class cannot be called from external source

```python
_dob = "01/02/12"
```
### Polymorphism
    - The condition of occurring in several forms.

# Different class names
- super
- base
- parent
- child
## Modules
Python modules are group of functions and tools that can be called by the user by using the key work import

### Lambda
- module that can be used to do maths function in one line
- any expression can be used in this function
```python
lambda Num1, Num2: Num2 + Num1
```
### key Word 
"Weekly sprint planning "


### OOP task1
```markdown

```
# Calculator class task
### MainCalc
- this file will be run to start the calculator 
```python
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

```

### calculator class
- holds the basic functions of the class 
````python
# create a calculator class
# add, subtract, multiply, divide, divisible
# extra Percentage, area of a triangle, inches to cm converter
# Divisible by the method that returns true or false depending on the outcome
# Work out and return the area of a triangle
# print(Nums())

class Calculator:  # define the class method

    def __init__(self):
        super().__init__()
        pass

    def add(Num1, Num2):  # addition function
        return Num1 + Num2

    def subtract(Num1, Num2):  # Subtraction function
        return Num1 - Num2

    def multiply(Num1, Num2):  # Multiply Function
        return Num1 * Num2

    def divide(Num1, Num2):  # Divide Function
        if Num2 == 0:  # error check to make sure the user doesnt enter 0 as you cannot divide by 0
            raise ZeroDivisionError  # this will raise an error in the programme that i will catch on the output of
            # the function
        else:  # if the numbers are valid it will return the answer for the division
            return Num1 / Num2

    def Nums():  # this function controls the users input making sure that the
        Num1 = input("Number 1 = ")  # these two lines control the users input for number 1 and 2
        Num2 = input("Number 2 = ")
        if Num1.isdigit() and Num2.isdigit():  # errors checks to make sure the user only can enter numbers
            Num1 = int(Num1)
            Num2 = int(Num2)
            return Num1, Num2
        else:  # if one or both is not a number it will run the following
            if not Num1.isdigit():  # this will  prints what ever the users entered and tell them it is not a valid
                # input
                print(f"{Num1} isn't a valid number")
            if not Num2.isdigit():  # checks for second number as well
                print(f"{Num2} isn't a valid number")
            print("Try again....\nEnter two valid Numbers")
            raise ValueError  # Raises a value error to be caught at the other end of the function

````
### Functional_calc class
- holds the more advance calc features
```python
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

```

# Movie rating class task
### Movie rating main
- this will start the programme 
```python
from Movie_rating import Movie_rating
from Movierating_Check import User_Check

class Movie_rating_main(Movie_rating, User_Check):

    def __init__(self):
        super().__init__()

    def Movie_Rating_main(self):
        while True:
            print("You can choose from the following")
            for ratings in Movie_rating.Movie_List.keys():
                print(ratings)
            user_rating = input("What rating do you want to know about?  ").lower()
            if Movie_rating_main.User_Exit(user_rating):
                return True
            elif not Movie_rating_main.User_Exit(user_rating):
                return False


    def User_Exit(User):
        if User() == "exit":
            return False
        else:
            print("Please enter a valid movie rating")

    def User_Input(User):

        if User in Movie_rating.Movie_List.keys():
            if User_Check(User):
                if input("Do you want to see another one? Y/N  ").upper() == "Y":
                    print("\n")
                    return True
                else:
                    return False

Movie_rating_main().Movie_Rating_main()
```

###Movie rating
- This is just a list that holds the move lists and definitions
```python
class Movie_rating:

    Movie_List = {

        "u": "everyone can watch",
        "pg": "General viewing, but some scenes may be unsuitable for young children",
        "12": "Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.",
        "15": "No one younger than 15 may see a 15 film in a cinema.",
        "18": "No one younger than 18 may see an 18 film in a cinema."
    }
```

### Movie check
- this class will be called to check the users input
```python
from Movie_rating import Movie_rating
from Movie_rating_main import Movie_rating_main


print(Movie_rating.Movie_List)

class User_Check(Movie_rating, Movie_rating_main):
    def __init__(self):
        super().__init__()

    def User_Check(Age):

        if Age == "exit":
            return False
        elif Age == "u":
            print(Movie_rating().Movie_List["u"])
            return True
        elif Age == "pg":
            print(Movie_rating().Movie_List["pg"])
            return True
        elif Age == "12":
            print(Movie_rating().Movie_List["12"])
            return True
        elif Age == "15":
            print(Movie_rating().Movie_List["15"])
            return True
        elif Age == "18":
            print(Movie_rating().Movie_List["18"])
            return True


```