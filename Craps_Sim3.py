# Craps Simulator
# Prints the value of two dice and their total for the number
#  of throws specified by "n" unless the user craps out.
#
# Variables Used:
#    n:       Number of times to throw the dice.
#    i:       Counter variable within "while" loop to count the number
#             of time the dice were thrown with 'n' being the max.
#             If a 'natural' (see below) is thrown, the rest of the
#             loop is skipped so the throw doesn't count.
#    throw_1: Value of the first die thrown.
#    throw_2: Value of the second die thrown.
#    total:   The sum of the two throws. (throw_1 + throw_2)
#    header:  A pre-defined header literal.
#    result:  Based on the special conditions, = one of several
#             possible strings. (win, loose, doubles, etc.)
#    point:   Stores the value of the current "point" that the player
#             needs to roll in order to win.
#
#             Point is also used as an end-of-game switch. "1 = end"
#             if the point was made, 7 was thrown, or the set number
#             of throws was exhausted. Each of these conditions will
#             cause the game to end.
#

import random

n = 10  # Max number of dice rolls per game
i = 1   # Starting increment for in-game dice rolls

header = "Die 1  Die 2  Total"  # Nice headers for display
result = ""  # Placeholder for the result string, when needed.
point = 0  # In craps, the "point" is the value the player needs
#            to throw to win.
throw_1 = 0  # First die
throw_2 = 0  # Second die
total = 0  # Sum of both dice

# Main
print("\nSimple Craps simulator\n")
print("Simplified rules:")
print("*  Make your point, you win.")
print("*  Make your point by rolling doubles, you win 2x the payout.")
print("*  Roll a seven before you make your point, you loose.\n")
print("*  There are a limited number of dice rolls, currently", n)
print("   If you run out of dice rolls before you make your point you loose.\n")
print("*  If you roll a two, (snake-eyes), you automatically loose.\n")
print("*  'Naturals', (12, 11, 7, 3, and 2), are automatically skipped")
print("   on your 'come-out' roll.\n")
print("*  Only 12, 11, and 3 are skipped when rolling for your point.")
print("   since 7 and 2 cause you to automatically loose.\n")

# Determine the point to make
print("Rolling for your 'come-out' point. . .")

# Determine the "come-out" point, (i.e. number to match)
#
while True:
    point = random.randint(2, 12)

# Is the selected point a 'natural'?
    if point == 12 or point == 11 or point == 7 or point == 3 or point == 2:
# If so, skip it and try again
        continue
    else:
        break

print("Your point to make is", str(point), "\n")
bogus = input("Press 'Enter' to begin\nGood Luck!\n")

print("Rolling to make your point...\n")
print(header)

while i < 11: # Interate from initial value of i to ten.
    throw_1 = random.randint(1, 6)
    throw_2 = random.randint(1, 6)
    total = throw_1 + throw_2

# Determine the result of this throw
# If the number thrown is a 'natural', it's skipped and doesn't count
# as a valid throw - I decrement "x" by one so that it doesn't count
    if total == 12 or total == 11 or total ==3:
#        print("Natural", str(total), "thrown! Skipping. . .")
        continue  # try again without incrementing the index
    if total == point:
        point = 1  # point=1 is set here to indicate end-of-game
        result = "WOW! You made your point so You Win!!"

# If the player throws doubles to make his point, he wins double        
        if throw_1 == throw_2:
            # overwrite result to indicate doubles
            result = "Hot Dog!! You rolled doubles to make your point!\n                     You win 2x the payout!"
    elif total == 7:
        result = "Seven Thrown!  You Loose!"
        point = 1  # point=1 is set here to indicate end-of-game
    elif total == 2:
        result = "Snake-Eyes!  You Crapped Out!"
    else:
        i = i
        result = ""

    print(str(throw_1).rjust(3), str(throw_2).rjust(6), str(total).rjust(6), '  ',result)
    if total < 3:
        break
    elif point == 1:
        break
    elif i == n:
        print("Sorry, you didn't make your point - you loose!")
    result = ""
    i = i + 1
print("\nTotal dice throws: ", i)
