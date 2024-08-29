# [ Task 1 ]

# Original
'''
attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
'''

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# The value must be cast to an int otherwise it is interpreted as a string.


# [ Task 2 ]

if venue == "large hall":
    print("We should have an audio speaker to reach everyone.")
    if attendees > 200:
        print("Prepare a LOT of food and other resources for consumption.")
elif venue == "conference room":
    print("Projector visible from anywhere, or several if 1 is not enough")
    if attendees > 80:
        print("Have good air conditioning to accomodate the amount of people in a small space.")
    

# [ Task 3 ]

food = input("would you like vegetarian food? ")
veg = False
if food == "yes":
    veg = True
# Assume non-vegetarian if answer is not yes

if venue == "large hall":
    print("We should have an audio speaker to reach everyone.")
    if attendees > 200:
        print("Prepare a LOT of food and other resources for consumption.")
elif venue == "conference room":
    print("Projector visible from anywhere, or several if 1 is not enough")
    if attendees > 80:
        print("Have good air conditioning to accomodate the amount of people in a small space.")

# Regardless of the venue, this option is given so it should not be included in both as it is redundant code.
if veg:
    print("You should try the Veggie Delight Caterers")
else:
    print("You should try the Gourmet Meals Caterers")