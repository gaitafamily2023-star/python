# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.


def simple_interest(p, r, t):
    return (p * r * t) / 100

# given values
interest = simple_interest(45000, 7, 8)
print("Simple Interest =", interest)

print("===================")

# loop calculations
principals = [30000, 60000]
rates = [5, 10]
times = [4, 6]

for i in range(2):
    print(
        "Simple Interest", i + 1, "=",
        simple_interest(principals[i], rates[i], times[i])
    )
