# A for loop can also be used to literate through a list, tuple, string or even adictionary...

name = "Kelvin"

for letter in name:
    if letter == "n":
        print("the letter is n")
    else:
        print(letter)

print('=====================')
# below is a list of counties
counties = ("Nairobi", "Mombasa", "Nakuru", "Embu", "Kisumu", "Machakos", "Kajiado", "Meru", "Nakuru")

for county in counties:
    print(county)

print('=====================')
if counties == "kitengela":
    print('county available')
else:
    print("county available")


print('=====================')
# The for loop can also be used to iterate through a dictionary




player = {
    'name' : "Mbappe",
    'age' : 25,
    'team' : ["PSG", "Morocco", "France"],
    'nationality' : "french"
}

for key in player:
    print(key)

print('=====================')
for value in player:
    print(player[value])


print('=====================')
# loop through the teams the player has played for
for value in player['team']:
    print(value)