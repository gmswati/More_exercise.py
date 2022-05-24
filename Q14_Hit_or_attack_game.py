from random import randint
from tabnanny import check
from turtle import hideturtle # allows you to generate a random number

# variables for the alien
alive = False
stamina = 10

# this function runs each time you attack the alien
def report(stamin):
# syntactic error in if else statements
    if stamin > 8:
        print ("The alien is strong! It resists your pathetic attack!")
        # print('stamina',stamin)
        return True
    elif stamin > 5:
        print ("With a loud grunt, the alien stands firm.")
        # print('stamina',stamin)
        return True
    elif stamin > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
        # print('stamina',stamin)
        return True
    elif stamin > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
        # print('stamina',stamin)
        return True
    else:
        print ("That's it! The alien is finished!")
        # print('stamina',stamin)
        return False


# main function - accepts your input for fight with the alien
def fight(stam): # stamina
    while stam > 0:
  # won't enter this loop ever. The function will always return False.
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run:\n").lower()
# chose a response from ( hit, attack, fight and run)
# fight scene
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            # print('less=',less)
            # less=7
            stam -= less # subtract random int from stamina
            report(stam) # see function above
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
        # return True
    #return False

print ("A threatening alien wants to fight you!\n")
# quotes at the end.

# call the function - what it returns will be the value of alive
alive = fight(stamina)

if alive: # means if alive == True
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("\nThe alien has been vanquished. Good work!\n")


# make it checked...
# Done! :)