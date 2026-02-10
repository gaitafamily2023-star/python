# loops -> sometime we may need to do a piece of work a number of times in such case we may use loops.
# A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python i.e : the loop and the while loop

# Below is the sytax of a for loop in python
"""
for variable in range(n)
    # block of code to be executed
"""


for greeting in range(50):
    print("hello Moses", greeting )

print('=====================')

for number in range(10, 20):
    print(number)




print('=====================')
# find the even numbers in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)


    print('=====================')
# create a python program that prints the odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

print('=====================')
# create a program that prints the muliples of 3 starting ftom 201 to 150

for number in range(201, 150, -3):
    print(number)

print('=====================')
# create a ython program that prints the leap yeas in between 2000 and 2024
for number in range(2000, 2025, 4):
    if number /400:
        print(number)