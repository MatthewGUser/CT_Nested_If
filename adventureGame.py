# [ Task 1 ]

# Original
'''
place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")
'''


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# No condition for else and = should be == when using comparotors to check if values match (in if statements)


# [ Task 2 ]

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("Do you want to light a torch or proceed?")
    if action == "light a torch":
        print("You light the torch.")
        print("You find a lot of gems.")
    elif action == "proceed":
        print("You proceed into the dark.")
        print("You are attacked.")




# [ Task 3 ]

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("Do you want to light a torch or proceed?")
    if action == "light a torch":
        print("You light the torch.")
        print("You find a lot of gems.")
    elif action == "proceed":
        print("You proceed into the dark.")
        print("You are attacked.")
    else:
        pass
else:
    pass