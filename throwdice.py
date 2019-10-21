# Function throw_dice
# takes a parameter of the number of sides
# defaulting to a six-sided die.
#
# returns an integer that is the value of the throw

def throw_dice(num_sides=6):
    """This function implements a generic dice throw.\n
The number of sides, (defaults to 6),\n"""
    import random
    import datetime
    myseed = int(datetime.datetime.timestamp(datetime.datetime.now())*1000000)
    random.seed(myseed)

    return random.randint(1, num_sides)
