# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# Converted List to a Dictionary without affecting the original code
# Just replaced '[]' by '{}'
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

# Created a dictionary
vocab = {"QUIT": "Q",
         "NORTH": "N",
         "SOUTH": "S",
         "EAST": "E",
         "WEST": "W",
         "ROAD": "1",
         "HILL": "2",
         "BUILDING": "3",
         "VALLEY": "4",
         "FOREST": "5"}

# # Not a part of the Challenge, just for the sake of understanding
# # It splits the location into separate words
# print(locations[0].split())

# # Splits by a comma
# print(locations[1].split(","))

# # Splits by a space in between
# print(' '.join(locations[0].split()))


loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        # We're copying all the locations in the exit dict into the variable allExits
        allExits = exits[loc].copy()
        # Now we're updating allExits variable with the dict of namedExits
        allExits.update(namedExits[loc])

    direction = input("Available Exits are " + availableExits + " ").upper()
    print()

    # We'll parse User Input using Vocab
    # If length of User entered word is > 1, then only proceed
    # This code is for checking the User Input (if it's a combination of strings),
    # then split the strings and find out the respective direction that matches and
    # hence print the appropriate result
    if len(direction) > 1:
        # Splitting the User Input
        words = direction.split()
        # Decalring a variable WORD for each single word in Words, if YES then proceed
        for word in words:
            # If the WORD is present in VOCAB, then combine it
            # with the respective direction
            if word in vocab:
                direction = vocab[word]
                break
#         # If the word is present in dict VOCAB then go ahead
#         for word in vocab:
#             # If the word exists in direction, then add the word in direction
#             # And find the appropriate location
#             if word in direction:
#                 # Now, if you type NORTH and hit enter it will match the word from the
#                 # VOCAB DICT and return the suitable result
#                 direction = vocab[word]

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")
