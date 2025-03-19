tall = int(input("Enter your Height: "))
credits = int(input("how many Credits you have?: "))

if tall >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif tall < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif tall >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("You have not met either requirement.")