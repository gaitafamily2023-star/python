distance = int(input("Enter distance traveled: "))

if distance >= 0 and distance <= 100:
    cost = 5.00
elif distance > 100 and distance <= 500:
    cost = 8.00
elif distance > 500 and distance < 1000:
    cost = 10.00
elif distance >= 1000:
    cost = 12.00
else:
    cost = 0
    print("Invalid distance")

print("Travel cost is:", cost)
