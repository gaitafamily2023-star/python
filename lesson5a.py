# python functions
# They are a block of code/statement that preform a given tasl=k/action. They can be reused through out to perform a different tasks.
# Functions are defined using the def keyword. (define)
# We have two main types of functions i.e:
# 1. In-built function -> they come preinstalled with the interpreter i.e print(), pop(), range(), append()etc.....
# 2. User defined functions => They are created by a programmer to  to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello, how are you?")


# below we call the function by use of its name
greetings()

print("=================================================")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

addition()

print("=================================================")
# create a function that  is able to multiply three values
def product():
    num4 = 5
    num5 = 6
    num6 = 10
    product = num4 * num5 * num6
    print("The product of the numbers are: ", product)

product()

print("=================================================")
# below is a division function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the secon number: "))
    quotient = number1 / number2
    print("The answer is: ", quotient)
    print("===========")


for function in range(3):
    divide()

