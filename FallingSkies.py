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



###  Move Left or Right ###

def go_left():
    """This function defines the movement of the player to the left of the screen"""
    player.direction = "left"
    player.shape("fbi.gif") 

def go_right():
        """This function defines the movement of the player to the right of the screen"""
    player.direction = "right"
    player.shape("fbi.gif") 
    
### Couple functions with keyboard ###
wn.listen() # The linking part 
wn.onkeypress(go_left, "Left") # when you press <-, the player moves to the left 
wn.onkeypress(go_right, "Right")# when you press ->, the player moves to the right


######## MAIN GAME ###########
##############################

while True:
    wn.update()

### Move the Player along the screen###

# Move left
    if player.direction == "left":
        x = player.xcor() 
        x = x-1 
        player.setx(x) 
        
# Move right    
    if player.direction == "right": 
        x = player.xcor() 
        x = x+1 
        player.setx(x) 



### Move benefits ###

# For every good guy in good_guys list gather y position and ajust it randomly
    for good_guy in good_guys: 
        y = good_guy.ycor() 
        y -= good_guy.speed 
        good_guy.sety(y) 

        if y < -300:
            x = random.randint(-580, 580) 
            y = random.randint(500, 600) 
            good_guy.goto(x, y) 
            
# If the distance from the good_guy to player is less than a pixel, adjust scoreboard and positions ; avoid screen overwrite
        if good_guy.distance(player) < 40: 
            x = random.randint(-580, 580) 
            y = random.randint(600, 600)
            good_guy.goto(x, y) 
            score += 10 
            pen.clear()
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Updating scoreboard


### Move hazards ###

# For every bad guy in good_guys list gather y position and ajust it randomly
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed 
        bad_guy.sety(y) 

        if y < -300:
            x = random.randint(-580, 580) 
            y = random.randint(600, 600)
            bad_guy.goto(x, y) 
            
# If the distance from the good_guy to player is less than a pixel, adjust scoreboard and positions ; avoid screen overwrite
        if bad_guy.distance(player) < 40: 
            x = random.randint(-580, 580) 
            y = random.randint(500, 600) 
            bad_guy.goto(x, y) 
            score -= 10 
            lives -= 1
            pen.clear() 
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) # Updating scoreboard
       

wn.mainloop()
