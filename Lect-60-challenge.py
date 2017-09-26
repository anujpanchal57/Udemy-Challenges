# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

SampleText = "Python is powerful"

# Frozen Set for VOWELS, so that it cannot be modified
vowels = frozenset("aeiou")

# Now for removing the vowels out of the final ouput, we can calculate the difference
# between SampleText and VOWELS as shown below and print the result
finalSet = set(SampleText).difference(vowels)
print(finalSet)

print(sorted(finalSet))