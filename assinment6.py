# simple intrest formular

principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time (years): "))

si = (principal * rate * time) / 100

print("Simple Interest is:", si)

print("===========================================")

# BMI Program

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)

print("===========================================")

# Area of Triangle

base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height

print("Area of Triangle is:", area)


print("===========================================")

# Area of a triangle

import math

radius = int(input("Enter the radius: "))

area = math.pi * radius ** 2

print("Area of the circle is: ", area)

print("===========================================")

shopping = {
    'sugar': 120,
    'rice': 200,
    'milk': 60,
    'bread': 60
}

print(shopping)

total = sum(shopping.values())
print("Total sum is:", total)

print("===========================================")

towns = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"]

towns.reverse()

print(towns)

