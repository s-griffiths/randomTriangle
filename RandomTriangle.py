# RandomTriangle.py
# This program calculates the expected values of the perimeter and
# area of a randomly generated triangle within a square with a side
# length of 5. The user chooses how many trials to run and
# is also allowed to run the simulation multiple times.

# import necessary libraries
import random
import math

# function to generate a random triangle inside a square with sides of length 5
def randomTriangle():

    # generate 3 random points
    ax = random.uniform(0,5)
    ay = random.uniform(0,5)
    bx = random.uniform(0,5)
    by = random.uniform(0,5)
    cx = random.uniform(0,5)
    cy = random.uniform(0,5)
     
    # uncomment to troubleshoot
    # print("ax =", ax, "ay =", ay)
    # print("bx =", bx, "by =", by)
    # print("cx =", cx, "cy =", cy)

    # length of the 3 sides
    a = math.sqrt((ax-bx)**2 + (ay-by)**2)
    b = math.sqrt((bx-cx)**2 + (by-cy)**2)
    c = math.sqrt((cx-ax)**2 + (cy-ay)**2)
    
    # semiperimeter according to Heron's Formula
    s = 0.5*(a + b + c)

    # perimeter
    perimeter = s * 2
    
    # area according to Heron's Formula
    area = math.sqrt(s*((s-a)*(s-b)*(s-c)))

    # returns perimeter and area of the triangle in a list
    return [perimeter, area]


# Main Program

# allows user to run the simulation multiple times
repeat = True
while repeat:

    # prompts the user for the number of trials to run
    userInput = input("Enter how many trials you want to run: ")

    # checks to see if the user entered a valid number of trials
    while True:
        try:
            numTrials = int(userInput)
        except:
            print("That is not valid input.")
            userInput = input("Try again: ")
            continue
        break



    # keeps the user from entering a negative number for the trials to run
    numTrials = int(userInput)
    if numTrials < 0:
        numTrials *= -1
    elif numTrials == 0:
        print("No trials were run.")
        break

    # list to hold the perimeter and area returned by each trial
    result = [0,0]


    # loop to run the trials
    for i in range(numTrials):
        triangle = randomTriangle()
        result[0] += triangle[0]
        result[1] += triangle[1]
        
        # uncomment to troubleshoot
        # print("Perimeter =", triangle[0])
        # print("Area =", triangle[1])


    # variables to hold expected values of perimeter and area
    avgPerimeter = result[0] / numTrials
    avgArea = result[1] / numTrials

    # output with explanation
    print("\nBased on three random points in a square with a side length of 5,")
    print("the triangle produced has an expected value of the")
    print("Perimeter =", avgPerimeter, "and of the Area =", str(avgArea) +".\n")

    # allows the user to quit or run the simulation again
    invalid = True
    while invalid:
        userInput = input("Do you want to run the simulation again [y/n]: ")
        if userInput == "y":
            repeat = True
            invalid = False
        elif userInput == "n":
            repeat = False
            invalid = False
        else:
            print("Invalid response.")
    print()
    
