# Challenge time!
# We have mentioned that the data for the Adventure game could be organised in many
# different ways.  We've created another way for you.
# Your mission, if you choose to accept it, is to
# change the code to make it work.
# Below is the the complete program from the last video, but with the
# locations dictionary modified so that everything is in a single dictionary.
# N.B. Yes the code has some errors, thats what you need to fix!

locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    # In this, we're changing EXITS dict to LOCATIONS dict and referring EXITS in that
    # as we don't have EXITS dict available as a separate dict, but in LOCATIONS dict,
    # We've EXITS as a sub-dictionary
    availableExits = ", ".join(locations[loc]["exits"].keys())

    # Because only printing the locations will not work we'll have to find out
    # description (DESC) from the master dictionary and access it in the print stmt
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        # As EXITS dict no longer exists, so we have to replace EXITS by LOCATIONS
        # master dict as given in the program and access the EXITS sub dict in it
        # After all this, we copy the contents of EXITS sub dict in the var allExits
        allExits = locations[loc]["exits"].copy()

        # After copying the contents in the allExits var, we'll update the namedExits
        # in the LOCATIONS master dict
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:   # does it contain a word we know?
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")