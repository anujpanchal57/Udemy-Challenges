# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

sample = ["Anuj", "Nidhi", "Radhika", "Viraj", "Aditi"]

# Iterator for above list
ravan_iterator = iter(sample)

# Loops for the number of times - 1 as and when compared with the list of items in SAMPLE
for char in range(0, len(sample)):
    # Prints the next item every time the loop runs
    print(next(ravan_iterator))