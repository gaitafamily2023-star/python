def area():
    length = 40
    width = 20
    area = length * width
    print("area", area)

area()


print("=============================================")

def calculate(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    division = a / b

    return sum, difference, product, division

result = calculate(20, 5)

print("Sum =", result[0])
print("Difference =", result[1])
print("Product =", result[2])
print("Division =", result[3])


print("=============================================")

def check():
    num = int(input("Enter number: "))

    if num > 0:
        print("number is positive")
    elif num < 0:
        print("number negative")
    else:
        print("Zero")

check()

print("=============================================")

def sumnum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

        print("sum from 1 to", n, "=", total)

sumnum(5)

print("=============================================")

def square_numbers():
    num = int(input("Enter a number: "))
    i = 1
    
    while i <= num:
        print("Square of", i, "=", i * i)
        i += 1

square_numbers()
