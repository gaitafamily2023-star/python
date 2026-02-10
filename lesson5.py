# functions with parameters
# Parameters: They are values that get passed as arguments given to a function inside of the parenthesis.


def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("Kelvin")
greeting("Mark")


print("========================================================")
def message(name):
    print(f"Hello {name}. We shall be having a geeral meeting on date........... Please avail yourself.")

message("Joy")
message("Kelvin")

print("========================================================")
# create function that accepts parameters to add two numbers
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 3)
add_numbers(10, 20)
add_numbers(78, 30)
