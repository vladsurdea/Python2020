# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:56:48 2020

@author: jmitc
"""
from Question import Question
import random


#questions for the quiz game
questions = [
    
    Question("Laura's eerily similar-looking cousin is named? \n (a) Maddy \n (b) Donna \n (c) Kathrin\n", "a"),
    Question("Dr. Jakobi hid half of Laura's necklace in a..? \n (a) Safe \n (b) Coconut \n (c) Old Shoe\n", "b"),
    Question("James Hurley drives a..? \n (a) Red Corvette \n (b) Rip-Stick \n (c) Harley-Davidson\n", "c"),
    Question("Agent Cooper likes his donuts filled with..? \n (a) Cream \n (b) Jelly \n (c) Mayonaise\n", "b"),
    Question("Audrey's last name rhymes with..? \n (a) Scorn \n (b) Furlough  \n (c) Blitz\n", "a"),
    Question("What color is Josie's lipstick? \n (a) Black \n (b) Red \n (c) Blue\n", "b"),
    Question("How many months was Hank in jail? \n (a) 23 \n (b) 10 \n (c) 18\n", "c"),
    Question("Pete left a fish in the percolator. \n (T) True \n (F) False\n", "T"),
    Question("Shelly concealed Leo's bloody shirt under the porch. \n (T) True \n (F) False\n", "F"),
    ]


#determined the number of questions answered correctly needed to win the game
WIN = (len(questions)//2)

#list of responses BOB gives you when you answer a question correctly
BOB_response_right = ["Looks like you know your stuff. But you won't get the next one right!"]

#list of questions when BOB answers you incorrectly
BOB_response_wrong = ["Hahahah, and you thought you could win!"]





def instructions():
    """Display the Instructions of the game"""
    print(
"""\n\nYou dare to traverse the falling skies! You dare to open the portal and enter the Black Lodge! \nYou have three lives and must answer 5 questions correctly to complete the game. Each question you get wrong I take one life away.\n\n""")

           

    

def valid_answer(answer,question):
    """checks if the value input for answer is a valid option"""
    VALID = ["a", "b", "c", "t","f"]
    while answer.lower() not in VALID:
        print("Why do you waste my time with invalid answers! Try again you fool.\n")
        print("\n\n" + question.prompt)
        answer = input(">> ")
    return True
        
#before you run the evaluate function you need a loop to determine when it breaks out
def evaluate(questions, position):
    """evaluate the answer and return True if correct and False if incorrect"""
    question = questions[position]
    print("\n\n" + question.prompt)
    answer = input(">> ")
    valid_answer(answer,question)
    if answer.lower() == question.answer.lower():
        return True
    else:
        return False


def score(questions):
    """governs the running total of both right and lives"""
    lives = 3
    right = 0
    position = 0
    random.shuffle(questions)
    while not lives==0 and not right == WIN:
        if evaluate(questions, position):
            right+=1
            if right < WIN -1:
                print("\n"+ random.choice(BOB_response_right))
        else:
            lives-=1
            if lives > 1:
                print("\n"+ random.choice(BOB_response_wrong))
        position+=1
        end_warning(lives, right)
    game_over(lives)
    
def end_warning(lives, right):
    """this fuction will print a warning that the game is nearing an end
    at either lives == 1 or  right == WIN - 1, and otherwise will return to the while loop
    driving score() function"""
    if lives == 1:
        print("\nYou have one life left! Muahahahahaha.")
    elif right == WIN - 1:
        print("\nYou only need one more correct answer to win... I see I underestimated you. But remember this, BOB NEVER LOSES!!!!")


def game_over(lives):
    """determines whether the player has won or lost"""
    if lives==0:
        print("All your bravery can't save you from ignorance! You have lost and Laura is forever MINE!!!!")
    else:
        print("Your may have defeated me but I'll be back! You haven't seen the last of BOB!!!")

def play():
    """this function will start the game if they player agrees, end the game if the player so chooses"""
    GO = ["y","n"]
    play =  input("Think you know your stuff? (y/n): \n\n>>")       
    while play not in GO:
        print("\nThat is an invaild answer!\n")
        play =  input("Do you want to play or not? (y/n)\n")
    if play == "y":
        print("\nMuahahahaha I hoped you would say that... ")
        return True
    else:
        print(""""\n\nYou Coward! You've come all this way and don't have the guts to walk with fire!BOB will forever remain in your nightmares, and the nightmares of Twin Peaks!""")
        return False
        





def main():
    """main function to run the program, requires no objects."""
    instructions()
    if play():
        score(questions)
    print(input("Press enter key to exit: "))
        


    
main() 

        
        




        
    
    


