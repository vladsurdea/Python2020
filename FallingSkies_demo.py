
# Importing turtle tool
import turtle
# Importing random tool
import random

score = 0
lives = 3

#Screen used for game/gameplay
wn = turtle.Screen()
wn.title("Falling Skies by @iNode.code") #Title of screen
wn.bgcolor("green")
wn.setup(width=800, height=600) # The height and width of screen
wn.tracer(0)



# Create Player
player = turtle.Turtle()
player.speed(0) # Animation speed fast as possible
player.shape("square") # Shape of player
player.color("white") # Color of player
player.penup() # Player wont draw 
player.goto(0, -250) # Start turtle the bottom
player.direction = "stop" # When game starts, player move left

# Create list of good guys
good_guys = []


# Create the good_guy
for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0) # Animation speed fast as possible //function speed
    good_guy.shape("square") # Shape of player
    good_guy.color("blue") # Color of player
    good_guy.penup() # Pen wont draw 
    good_guy.goto(-100, 250) # Start turtle from top left
    good_guy.speed = random.randint(1, 2) # Random speed between 1 & 2 for each good guy //This speed is a variable
    good_guys.append(good_guy) # Adding each good_guy to good_guys list

# Create list of bad guys
bad_guys = []

# Create the bad_guy
for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0) # Animation speed fast as possible //function speed
    bad_guy.shape("square") # Shape of player
    bad_guy.color("red") # Color of player
    bad_guy.penup() # Player wont draw 
    bad_guy.goto(100, 250) # Start turtle the bottom
    bad_guy.speed = random.randint(1, 2) # Random speed between 1 & 4 for each good guy //This speed is a variable
    bad_guys.append(bad_guy) # Adding each good_guy to good_guys list

# Create Pen
pen = turtle.Turtle() # Turtle object
pen.hideturtle() # Wont show pen on screen
pen.speed(0) # Animation speed fast as possible
pen.shape("square") # Shape of player
pen.color("white") # Color of player
pen.penup() # Player wont draw 
pen.goto(0, 260) # Position of where the pen writes
font = ("Courier", 24, "normal") # Font type, size 24, normal font
pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Displays scores and lives on screen



# Functions         //Think of functions as helper programs, within a program
def go_left():
    player.direction = "left"
    player.shape("square") # Original or left facing

def go_right():
    player.direction = "right"
    player.shape("square") # right facing
    

# Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


#Main Game Loop
#While this is true, repeat
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
    for good_guy in good_guys: # For every good guy in good_guys list
        y = good_guy.ycor() # Gather his y position
        y -= good_guy.speed # utilizing the random tool in good_guy
        good_guy.sety(y) # Set position


        # check if off the screen
        if y < -300:
            x = random.randint(-380, 380) # Random tool to make game interesting, screen is 400x400
            y = random.randint(300, 400) # Start off screen?
            good_guy.goto(x, y) # Start from top

        # Check for a collision with the player
        if good_guy.distance(player) < 40: # If the distance from the good_guy to player is less than 40 //pixels are 40x40
            x = random.randint(-380, 380) # Random tool to make game interesting, screen is 400x400
            y = random.randint(300, 400) # Start off screen?
            good_guy.goto(x, y) # Start from top
            score += 10 # Increases score by 10
            pen.clear() # To avoid overwriting on screen
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Updating and displaying score when collision accurs



# Move the bad guys
    for bad_guy in bad_guys: # For every bad guy in bad_guys list
        y = bad_guy.ycor() # Gather his y position
        y -= bad_guy.speed # utilizing the random tool in bad_guy
        bad_guy.sety(y) # Set position

        # check if off the screen
        if y < -300:
            x = random.randint(-380, 380) # Random tool to make game interesting, screen is 400x400
            y = random.randint(300, 400) # Start off screen?
            bad_guy.goto(x, y) # Start from top

        # Check for a collision with the player
        if bad_guy.distance(player) < 40: # If the distance from the bad_guy to player is less than 40 //pixels are 40x40
            x = random.randint(-380, 380) # Random tool to make game interesting, screen is 400x400
            y = random.randint(300, 400) # Start off screen?
            bad_guy.goto(x, y) # Start from top
            score -= 10 # Decreases score by 10
            lives -= 1 # Everytime we collide with bad guy, take away one life
            pen.clear() # To avoid overwriting on screen
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Updating and displaying score when collision accurs
       
wn.mainloop()
