# Stores Name and Age of the person
name = input("Please enter your name : ")
age = int(input("What is your age : "))

# Checks whether he/she is below 18 or above 31
if 18 <= age < 31:
    print("Welcome to the Holiday Mr. {} !!!".format(name))

# If he/she is below 18 years of age or above 31 years of age
# Then he/she is not eligible for the party
else:
    print("Sorry you aren't eligible for the holiday :( ")