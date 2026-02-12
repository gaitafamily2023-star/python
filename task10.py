def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

result = calculate_bmi(70, 1.75)
print("BMI is:", result)
