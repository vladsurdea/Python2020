"""
Created on Fri Dec 4 12:50 2020
@author: Vlad Surdea-Hernea
"""

"""Falling Skies
The following script uses the turtle module in order to use basic graphics in Python, 
and the random module in order to make random numbers used for the dynamics of the game.

The game puts the player in the shoes of Agen Cooper that needs to avoid the poisonous
hazards droping from the sky, while also collecting the beneficial suitcases 
—proper for an FBI agent! 

"""

import turtle ### allows for basic graphics
import random ### will help us set some random elements for the game


######## PRE-GAME ###########
##############################

### Set up the number of lives and the initial score ###
score = 0
lives = 3


### Import "screen" and adjust settings ###
wn = turtle.Screen() # Create the gamescreen
wn.title("Falling Skies: Fire,Fire Walk with Me") # Add the title of the game
wn.bgpic("Back.gif") # Add the background for the screen
wn.setup(width=800, height=600) # Set the dimensions for the screen
wn.tracer(0) # Optimize drawings for MacOS


### Import pictures for character sprites ###
wn.register_shape("fbi.gif")  # Agen Cooper
wn.register_shape("poison.gif") # Hazards
wn.register_shape("rsz_suitcase.gif") # Benefits


### Create the player ###
player = turtle.Turtle() # import object
player.speed(0) # Set the animation speed
player.shape("fbi.gif") # Set the picture to be used for the sprire
player.color("white") # Color of player
player.penup() # Set player such as it won't draw 
player.goto(0, -250) # Start position
player.direction = "stop" # When game starts, the sprite should move left

### Create list of benefits ###
good_guys = [] #empty list to be filled by "good guys"

for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0) # Animation speed 
    good_guy.shape("rsz_suitcase.gif") # Shape 
    good_guy.penup() # Wont draw 
    good_guy.goto(-100, 250) # Startfrom top left
    good_guy.speed = random.randint(1, 2) # Random speed
    good_guys.append(good_guy) # Adding each good_guy to good_guys list

### Create list of hazards ###
bad_guys = [] #empty list to be filled by "bad guys"
for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0) # Animation speed 
    bad_guy.shape("poison.gif") # Shape 
    bad_guy.penup() # Player wont draw 
    bad_guy.goto(100, 250) # Start at the bottom
    bad_guy.speed = random.randint(1, 2) # Random speed b
    bad_guys.append(bad_guy) # Adding each good_guy to good_guys list

### Create scoreboard ###
pen = turtle.Turtle() # Import turtle object
pen.hideturtle() # Do not show the object
pen.speed(0) # Set speed
pen.shape("square") # Shape 
pen.color("white") # Color 
pen.penup() # Wont draw 
pen.goto(0, 260) # Position of where the pen writes
font = ("Courier", 24, "normal") # Font type and size
pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Displays scores and lives on screen





# Functions         //Think of functions as helper programs, within a program
def go_left():
    """Function that defines moving to the left"""
    player.direction = "left"
    player.shape("fbi.gif") 

def go_right():
    """Function that defines moving to the right"""
    player.direction = "right"
    player.shape("fbi.gif") 
    

# Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


######## PRE-GAME ###########
##############################

while True:
    # Update screen
    wn.update()

    # Move the Player
    if player.direction == "left": # -x Coordinate
        x = player.xcor() # Stores the xcor of player in x, starts at 0 on X axis
        x -= 1 # minus 1 from x, this will repeat because it is true
        player.setx(x) # Set coordinate
    
    if player.direction == "right": # -x Coordinate
        x = player.xcor() # Stores the xcor of player in x, starts at 0 on X axis
        x += 1 # minus 1 from x, this will repeat because it is true
        player.setx(x) # Set coordinate    



    # Move the good guys
    for good_guy in good_guys: 
        y = good_guy.ycor() 
        y -= good_guy.speed 
        good_guy.sety(y) 


        # check if off the screen
        if y < -300:
            x = random.randint(-380, 380) # Random tool to make game interesting, screen is 400x400
            y = random.randint(300, 400) 
            good_guy.goto(x, y) 

        # Check for a collision with the player
        if good_guy.distance(player) < 40: # Check if the distance from the bad_guy to player is less than a pixel
            x = random.randint(-380, 380) 400
            y = random.randint(300, 400) 
            good_guy.goto(x, y) 
            score += 10 # Increases score by 10
            pen.clear() # To avoid overwriting on screen
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Updating scoreboard



# Move the hazards
    for bad_guy in bad_guys: 
        y = bad_guy.ycor() 
        y -= bad_guy.speed
        bad_guy.sety(y) 

        # check if off the screen
        if y < -300:
            x = random.randint(-380, 380) # Random tool to make game interesting, screen is 400x400
            y = random.randint(300, 400) # Start off screen?
            bad_guy.goto(x, y) # Start from top

        # Check for a collision with the player
        if bad_guy.distance(player) < 40: # Check if the distance from the bad_guy to player is less than a pixel
            x = random.randint(-380, 380) 
            y = random.randint(300, 400) 
            bad_guy.goto(x, y) 
            score -= 10 # Decreases score 
            lives -= 1 # Lose one life
            pen.clear() # Avoid overwriting on screen
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Updating scoreboard
       
wn.mainloop()

