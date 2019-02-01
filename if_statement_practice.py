#Basic if statement
#
v = int(input("enter a number from 10 to 20 "))
if v == 15:
    print ("i thought you might choose that number")
else:
    print ("i guessed the wrong number")

#Basic Elif statement
#
v = int(input("enter a number from 1 to 20 "))
if v == 15:
    print ("i thought you might choose that number")
elif v > 1: print ("I said..enter a number from 1 to 20 ")          #single statement suite for simple statements
elif v < 20:
    print ("I said..enter a number from 1 to 20 ")
else:
    print ("i guessed the wrong number")
#
# Code cleanup
#
v = int(input("enter a number from 1 to 20 "))
if v == 15: print ("i thought you might choose that number")            #single statement suite for simple statements
elif v > 1 and v < 20: print ("I said..enter a number from 1 to 20 ")   #single statement suite for simple statements
else:                                                                   #tailing 'else' is not mandatory code, see below
    print ("i guessed the wrong number")
#
#Nested Elif statement
#
#
age = input ("Are you an adult or a child?")
tod = input ("is it day or night?")

if age == 'adult':
    if tod == 'day':
        cost = 7
    elif tod == 'night':
        cost = 15
elif age == "child":
    if tod == "day": cost = 4
    elif tod == "night": cost = 8

print ("The", age, "ticket will cost you", cost, "dollars")
