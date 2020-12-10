"""
Created on Fri Nov 20 14:56 2020

@author: sofiasukhova
"""

"""Text-based adventure game

This script uses 'sys' module for quitting the game (through sys.exit() command)
and applying text effects.
'Time' module is used for other special effects:

time.sleep()
Each line of text is coded to appear after several seconds
depending on the length of a line, giving the player time
to read the text properly
(from 4 to 6 seconds).

time.sleep(c)
Some lines appear letter by letter, creating
an effect of exclamation or questioning.

The game begins with title screen (in the bottom of the script)."""

import sys
import time

a = 4
b = 0.2
c = 0.08
d = 2
e = 1
f = 6

def intro():
    """The starting point of the game."""

    print()
    time.sleep(d)
    print("Congratulations! You’ve collected all scrolls to find a portal to the Black Lodge!")
    time.sleep(a)
    print()
    print("You open the scrolls and read the following message:")
    time.sleep(e)
    print()
    time.sleep(e)
    print()
    time.sleep(e)
    print()
    time.sleep(a)
    s1 = "“   For you to find a way"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
        """Text appears character by character.
        
        Time interval is 0.08 seconds."""

    print()
    time.sleep(a)
    s2 = "    You shall lead a path astray;"
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
        """Text appears letter by letter."""

    print()
    time.sleep(a)
    s3 = "    Into the woods, far away."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
        """Text appears letter by letter."""

    print()
    time.sleep(a)
    s4 = "    Beware: spirits like foul play.  “"
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
        """Text appears letter by letter."""

    print()
    time.sleep(e)
    print()
    time.sleep(e)
    print()
    time.sleep(a)
    print("You walk out of the cave, it's getting darker. What is your next move?")
    print()
    time.sleep(a)
    print("1. Drive in the police car back to the Great Northern hotel")
    time.sleep(a)
    print("2. Drive deep into the forest")
    time.sleep(a)
    print("3. Walk on foot")
    print()
    time.sleep(a)
    firstPath = input("Which path will you choose? (1/2/3): ")
    """First choice.
    
    Type 1, 2 or 3 to proceed."""

    if firstPath == '1':
        """Game proceeds to path1."""

        print()
        path1()
    elif firstPath == '2':
        """Game proceeds to path2."""

        print()
        path2()
    elif firstPath == '3':
        """Game proceeds to path3."""

        print()
        path3()

def path1():
    """Path1 - wrong choice."""

    print()
    time.sleep(a)
    s5 = "Only tonight the portal can be opened..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
        """Text appears letter by letter."""

    print()
    time.sleep(a)
    print()
    print(" ### Game Over ### ")
    time.sleep(a)
    sys.exit()
    """Game terminates."""


def path2():
    """Path2 - proceeds to path3."""

    time.sleep(a)
    print("Your car breaks down eventually in the middle of the woods.")
    time.sleep(a)
    print("It's dark outside. You have to move on and get out of the car.")
    print()
    path3()

def path3():
    """Path3 - storyline continues."""

    time.sleep(a)
    print("You decide to walk on foot.")
    time.sleep(a)
    print("You start hearing strange voices.")
    time.sleep(a)
    print("Something is moving in the bushes...")
    time.sleep(a)
    print("It's a fox! What do you do?")
    print()
    time.sleep(a)
    print("1. Pet it, of course!")
    time.sleep(a)
    print("2. Wait and observe - maybe it's just a fox")
    time.sleep(a)
    print("3. Run! It might be a spirit!")
    print()
    time.sleep(a)
    secondPath = input("What will you do? (1/2/3): ")
    """Second choice.

        Type 1, 2 or 3 to proceed."""

    if secondPath == '3':
        """Game proceeds to path4."""

        print()
        time.sleep(a)
        print("You run through the darkness too scared to think where you are heading.")
        path4()
    else:
        """Game continues."""

        print()
    time.sleep(a)
    print("You were right, it is just a fox!")
    time.sleep(a)
    print("It sniffs your hand, and you pet it gently.")
    time.sleep(a)
    print("But wait - it lures you somewhere.")
    time.sleep(a)
    print("You follow it and arrive at an abandoned wooden hut with red light streaming from the windows.")
    time.sleep(a)
    print("What is your next move?")
    print()
    time.sleep(a)
    print("1. Walk inside")
    time.sleep(a)
    print("2. Peek inside the windows")
    time.sleep(a)
    print("3. Run away")
    print()
    time.sleep(a)
    thirdPath = input("What will you do? (1/2/3): ")
    """Third choice.

        Type 1, 2 or 3 to proceed."""

    if thirdPath == '1':
        """Wrong path.
        
        Game ends after final messages."""

        print()
        time.sleep(a)
        s6 = "Too bad, the spirits appear and catch you, trapping you inside the house."
        for character in s6:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        time.sleep(a)
        s7 = "The scrolls warned you, “spirits like foul play“!"
        for character in s7:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        time.sleep(a)
        print()
        s8 = " ### Game Over ### "
        for character in s8:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        time.sleep(a)
        sys.exit()
        """Game terminates."""

    elif thirdPath == '2':
        """Game proceeds to path4."""

        print()
        time.sleep(a)
        print("You notice weird shapes of people, but they are not human - those are evil spirits!")
        time.sleep(a)
        print("Your fox friend turned out to be a cunning one.")
        time.sleep(a)
        print("You decide to leave this place and notice a waterfall noise in the distance.")
        time.sleep(a)
        print("You follow its sounds...")
        time.sleep(a)
        print()
        path4()
    elif thirdPath == '3':
        """Game proceeds to path4."""

        print()
        time.sleep(a)
        print("You run through the darkness too scared to think where you are heading.")
        print()
        path4()

def path4():
    """Path4 - storyline continues."""

    time.sleep(a)
    print("Eventually, you reach a foot of a mountain, a gentle waterfall makes its way into a river nearby.")
    time.sleep(a)
    print("You notice a cave behind it - would you go inside?")
    print()
    time.sleep(a)
    print("1. Well of course! Maybe there is a clue to where the portal might be located.")
    time.sleep(a)
    print("2. No more shady adventures for me! Better keep going into the woods.")
    print()
    time.sleep(a)
    fourthPath = input("Your decision? (1/2): ")
    """Fourth choice.

    Type 1 or 2 to proceed."""
    if fourthPath == '2':
        """Wrong path.

        Game ends after final messages."""

        print()
        time.sleep(a)
        print("No more shady adventures for me! ")
        time.sleep(a)
        print("Better keep going into the woods.")
        print()
        time.sleep(a)
        print("You walk in circles but suddenly find your way back to Twin Peaks.")
        time.sleep(a)
        s9 = "Bummer, you've failed your mission!"
        for character in s9:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        print()
        time.sleep(a)
        s10 = " ### Game Over ### "
        for character in s10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        sys.exit()
        """Game terminates."""

    elif fourthPath == '1':
        """Game proceeds to path5."""

        print()
        path5()

def path5():
    """Path5 - storyline continues."""

    time.sleep(a)
    print("You step inside, hollow sounds of your footsteps echo in the darkness of the cave.")
    time.sleep(a)
    print("You go further with your torch and eventually stand before... a door?")
    time.sleep(a)
    print("Looks like someone's retreat!")
    print()
    time.sleep(a)
    print("The door was unlocked, you come inside and find yourself in a peculiar room decorated as if it was a magician's office.")
    time.sleep(a)
    print("You stand in front of a desk.")
    time.sleep(a)
    print("The Log Lady sits there!")
    time.sleep(a)
    print("She was waiting for you to arrive, the log told her about your adventures and the mission you are following.")
    time.sleep(a)
    print("She makes you a cup of “ damn fine“  coffee and invites you to sit down.")
    time.sleep(a)
    print()
    print("1. You take the cup and drink the coffee")
    time.sleep(a)
    print("2. You wait for her to speak")
    time.sleep(a)
    print("3. You politely refuse to drink")
    print()
    time.sleep(a)
    fifthPath = input("Your next move? (1/2/3): ")
    """Fifth choice.

    Type 1, 2 or 3 to proceed."""

    if fifthPath == '1':
        """Game proceeds to path6."""

        print()
        time.sleep(a)
        print("She interrupts you before you could drink any more, asks you to place the cup back on the table, and you witness the following scene...")
        print()
        path6()
    elif fifthPath == '2':
        """Game proceeds to path6."""

        print()
        path6()
    elif fifthPath == '3':
        """Game proceeds to path6."""

        print()
        time.sleep(a)
        print("She smiles and you witness the following scene...")
        path6()

def path6():
    """Path6 - storyline continues."""

    time.sleep(a)
    print("She starts practicing divination on the coffee cup: ")
    time.sleep(f)
    print("Rain clouds appear above the black liquid - a premonition for stormy times ahead.")
    time.sleep(f)
    print("She wishes you all the best fortune and whispers in your ear: “Find Her“...")
    time.sleep(e)
    print()
    time.sleep(e)
    print()
    time.sleep(a)
    print()
    time.sleep(a)
    print("You walk out of the cave confident on your next step.")
    time.sleep(e)
    print()
    time.sleep(f)
    print("Eventually, you reach a clearing and you find yourself standing in the middle of a large field with tall grass.")
    time.sleep(f)
    print("You notice that the grass doesn't grow uniformly - it forms an intricate maze!")
    print()
    time.sleep(f)
    print("You turn different paths and encounter many spirits glowing red...")
    time.sleep(f)
    print("They see you but do not attack, they simply observe you moving through the maze.")
    print()
    time.sleep(f)
    print("You make your way into the middle of the field where you see a wooden house hovering above the grass.")
    time.sleep(f)
    print("A young girl appears in front of you - it looks like she is made of fire itself.")
    time.sleep(f)
    s11 = "Could that be... Laura Palmer?!"
    for character in s11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
        """Text appears letter by letter."""

    print()
    print()
    time.sleep(f)
    print("You stare at her in awe, she is glowing fiery orange.")
    time.sleep(f)
    print("Then she whispers, “Fire, fire walk with me...“")
    time.sleep(f)
    print("You are trying to comprehend the meaning of this phrase when the house behind her sets on fire.")
    time.sleep(f)
    print("She shows you a mirror and you see yourself transforming - now you look like her, shining like fire.")
    time.sleep(f)
    print("You both walk through the entrance of the burning house while saying the phrase that has been lingering in your mind all this time...")
    time.sleep(f)
    password = input("Please type the phrase here (think carefully...): ")
    """Correct phrase is required to proceed.
    
    Player has to type the phrase he/she encountered in the beginning
    of the game. Incorrect input leads to game termination."""

    if password == 'spirits like foul play' or password == 'Spirits like foul play' or password == 'Spirits Like Foul Play':
        """Correct inputs.
        
        The player can proceed to play game #3."""

        print()
        time.sleep(a)
        s12 = "Congratulations! You opened a portal to the Black Lodge!"
        for character in s12:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        print()
        time.sleep(f)
        sys.exit()
        """Game ends."""

    else:
        """The input is incorrect.
        
        The game ends, and the player has to start over.
        Several final messages appear."""

        print()
        time.sleep(a)
        s13 = "You fail to name the password to open the Black Lodge entrance."
        for character in s13:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        time.sleep(a)
        s14 = "The whole journey was in vain, and you have to start anew."
        for character in s14:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        time.sleep(a)
        s15 = "~Spirits like foul play!~"
        for character in s15:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        time.sleep(a)
        print()
        time.sleep(a)
        s16 = " ### Game Over ### "
        for character in s16:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
            """Text appears letter by letter."""

        print()
        time.sleep(f)
        sys.exit()
        """Game terminates."""





print()
print("   #############################   ")
print("   #                           #   ")
print("   #  Fire, Fire Walk With Me  #   ")
print("   #          Part II          #   ")
print("   #                           #   ")
print("   #############################   ")
print()
print()
time.sleep(a)
startGame = input("Start the game? (Yes/No): ")
"""Asks the user to start or quit the game.

To start the game, type either of these commands:
yes, Yes, y, Y.
To quit the game, type any of the following:
no, No, n, N."""

if startGame == 'no' or startGame == 'No' or startGame == 'n' or startGame == 'N':
    """Game quits if any 'No' command above is typed."""

    time.sleep(b)
    print("Until next time then...")
    time.sleep(a)
    sys.exit()
    """Game terminates."""

elif startGame == 'yes' or startGame == 'Yes' or startGame == 'y' or startGame == 'Y':
    """The game is launched if any 'Yes' command above is typed."""

    intro()