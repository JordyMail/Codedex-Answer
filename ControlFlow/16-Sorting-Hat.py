Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Answer it with the number of its answer!")

print("Q1) Do you like Dawn or Dusk?")
print(" 1) Dawn")
print(" 2) Dusk")

one = int(input("Your answer: "))

if one == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif one == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input!")

print("Q2) When I’m dead, I want people to remember me as:")
print(" 1) The Good")
print(" 2) The Great")
print(" 3) The Wise")
print(" 4) The Bold")

two = int(input("Your answer: "))
if two == 1:
    Hufflepuff += 2
elif two == 2:
    Slytherin += 2
elif two == 3:
    Ravenclaw += 2
elif two == 4:
    Gryffindor += 2
else:
    print("Wrong input!")

print("Q3) Which kind of instrument most pleases your ear?")
print(" 1) The violin")
print(" 2) The trumpet")
print(" 3) The piano")
print(" 4) The drum")

three = int(input("Your answer: "))

if three == 1:
    Slytherin += 4
elif three == 2:
    Hufflepuff += 4
elif three == 3:
    Ravenclaw += 4
elif three == 4:
    Gryffindor += 4
else:
    print("Wrong input!")

print("Slytherin: " + str(Slytherin))
print("Hufflepuff: " + str(Hufflepuff))
print("Ravenclaw: " + str(Ravenclaw))
print("Gryffindor: " + str(Gryffindor))
