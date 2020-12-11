 # -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:56:48 2020

@author: jmitc
"""
from Question import Question
import random
import time
import pyfiglet


#questions for the quiz game
questions = [
    
    Question("Laura's eerily similar-looking cousin is named? \n (a) Maddy \n (b) Donna \n (c) Kathrin\n", "a", ["a", "b", "c"]),
    Question("Dr. Jakobi hid half of Laura's necklace in a..? \n (a) Safe \n (b) Coconut \n (c) Old Shoe\n", "b", ["a", "b", "c"]),
    Question("James Hurley drives a..? \n (a) Red Corvette \n (b) Rip-Stick \n (c) Harley-Davidson\n", "c", ["a", "b", "c"]),
    Question("Agent Cooper likes his donuts filled with..? \n (a) Cream \n (b) Jelly \n (c) Mayonaise\n", "b", ["a", "b", "c"]),
    Question("Audrey's last name rhymes with..? \n (a) Scorn \n (b) Furlough  \n (c) Blitz\n", "a", ["a", "b", "c"]),
    Question("What color is Josie's lipstick? \n (a) Black \n (b) Red \n (c) Blue\n", "b", ["a", "b", "c"]),
    Question("How many months was Hank in jail? \n (a) 23 \n (b) 10 \n (c) 18\n", "c", ["a", "b", "c"]),
    Question("Pete left a fish in the percolator. \n (T) True \n (F) False\n", "T", ["t", "f"]),
    Question("Shelly concealed Leo's bloody shirt under the porch. \n (T) True \n (F) False\n", "F", ["t", "f"]),
    Question("'Diane' is the name of Cooper's assistant back at headquarters. \n (T) True \n (F) False\n", "T", ["t", "f"]),
    Question("Twin Peaks is blessed to be surrounded by a forest of Cottonwood Firs. \n (T) True \n (F) False\n", "F", ["t", "f"]),
    Question("Who killed Laura Palmer? \n (a) Deputy Hawk \n (b) Bobby \n (c) Leland Palmer\n", "c", ["a", "b", "c"]),
    Question("What is the name of Ben Horne's hotel? \n (a) The White Lodge \n (b) The Great Northern  \n (c) The Grand Peaks\n", "b", ["a", "b", "c"]),
    Question("When does Laura tell Agent Cooper she'll see him again? \n (a) 25 Years \n (b) 10 Months \n (c) After his death\n", "a", ["a", "b", "c"]),
    Question("Nadine buys cotton balls to make what ingenious invention? \n (a) Injury-Free Trampoline \n (b) Silent Drapes \n (c) The Perfect Mop\n", "b", ["a", "b", "c"]),
    Question("Who is Donna's biological father? \n (a) Dr. Will Wayward \n (b) Dr. Jakobi \n (c) Ben Horne\n", "b", ["a", "b", "c"]),
    Question("Who was Ed Hurley's high school sweetheart? \n (a) Norma Jennings \n (b) Nadine Hurley \n (c) Josie Packard\n", "a", ["a", "b", "c"]),
    Question("It was Pete Martell that first discovered Laura's body. \n (T) True \n (F) False\n", "t", ["t", "f"]),
    Question("What is the alias of The Man From Another Place? \n (a) The Creeper \n (b) Mike \n (c) The Arm\n", "c", ["a", "b", "c"]),
    Question("What is the name of the popular diner in Twin Peaks? \n (a) Twin Diner \n (b) The Triple R  \n (c) The Double R\n", "c", ["a", "b", "c"])
    ]


#determines the number of questions answered correctly needed to win the game
WIN = (len(questions)//2)

#list of responses BOB gives you when you answer a question correctly
bob_response_right = ["Looks like you know your stuff. But you won't get the next one right!",
                      "Don't get too confident there bub! BOB knows all and knows you can't hack it.",
                      "Ha! That one was an easy one.",
                      "Any pee-brain knows that.",
                      "GRRGGRH!!!",
                      "You may know that, but I know you'll never escape!",
                      "WHO TOLD YOU THE ANSWERS!!",
                      "You're laughing now but just wait for the next one!"]


#list of responses BOB gives you when you answer a question incorrectly
bob_response_wrong = ["Hahahah, and you thought you could win!",
                      "MMMMMMMMmmm I just ate one of your DELICIOUS lives.",
                      "You fool! Are you even a real detective?",
                      "This is gonna be easier than I thought.",
                      "You'll never make it out of here alive!",
                      "One more life for me!!",
                      "BOB is too clever! Ahahahaha.."]


you_win = pyfiglet.figlet_format("you win") 
you_lose = pyfiglet.figlet_format("you lose")



def instructions():
    """Display the Instructions of the game."""
    time.sleep(2.0)
    welcome = pyfiglet.figlet_format("WELCOME!!")
    bob = pyfiglet.figlet_format("BOB")
    ascii_banner = pyfiglet.figlet_format("HA!!")
    print(welcome)
    time.sleep(1.2)
    print("\n\n... to the Black Lodge")
    time.sleep(2.5)
    print("\n\nYou dared to traverse the falling skies!")
    time.sleep(2.5)
    print("\n\nYou dared to open the portal and enter my hangout!")
    time.sleep(2.5)
    print("\n\nWell now you've found me:")
    time.sleep(1.5)
    print(bob)
    time.sleep(1.0)
    for i in range(18):
        time.sleep(.3)
        print("HA")
    time.sleep(.5)
    print(ascii_banner)
    time.sleep(1.0)
    print("...")
    time.sleep(1.0)
    print("...")
    time.sleep(2.0)
    print("\n\nAnd now for the rules of our little game..")
    time.sleep(2.5)
    print("\n\nYou have three lives and must answer", WIN, "questions correctly to win.")
    time.sleep(2.5)
    print("\n\nEach question you get wrong I take one life away.\n\n")
    time.sleep(2.5)
    

    

def valid_answer(answer,question):
    """
    Checks if the answer is a valid option and returns True once a valid answer 
    is input.
    
    Parameters:
        answer (str): user input 
        question (Question): question chosen from questions based on position
    
    """
    while answer.lower() not in question.options:
        time.sleep(1.0)
        print("\n\nWhy do you waste my time with invalid answers! Try again you fool.\n")
        time.sleep(2.0)
        print("\n\n" + question.prompt)
        answer = input(">> ")
    return True
        

def evaluate(questions, position):
    """
    Evaluate the answer and return True if correct and False if incorrect
    
    Parameters:
        questions (list): the list of questions
        position (value): position in list of questions
    
    Returns:
        answer (str): user input
        question (Question): question chosen from questions based on position
    
    """
    question = questions[position]
    print("\n\n" + question.prompt)
    answer = input(">> ")
    valid_answer(answer,question)
    if answer.lower() == question.answer.lower():
        return True
    else:
        return False


def score(questions):
    """
    Receives value from the evaluate function to keep score, as well as 
    propells the value corresponding to the next question.
    
    Parameters:
        questions (list): the list of questions
    
    Returns:
        lives (value): number of lives left
        right (value): number of questions answered correctly
        position (value): position in list of questions
    
    """
    lives = 3
    right = 0
    position = 0
    random.shuffle(questions)
    while not lives==0 and not right == WIN:
        if evaluate(questions, position):
            right+=1
            if right < WIN -1:
                print("\n"+ random.choice(bob_response_right))
                time.sleep(3.0)
        else:
            lives-=1
            if lives > 1:
                print("\n"+ random.choice(bob_response_wrong))
                time.sleep(3.0)
        position+=1
        end_warning(lives, right)
    #return the lives and right values and take the game over function out
    game_over(lives)
    
def end_warning(lives, right):
    """
    Prints a warning that the user has one life left or if the user is one 
    correct answer away from winning the game.
    
    Parameters:
        right (value): the number of questions answered correctly
        lives (value): the number of lives left
    
    """
    if lives == 1 and not right >= WIN -1:
        print("\nYou have one life left! Muahahahahaha.")
    elif right == WIN - 1:
        print("\nYou only need one more correct answer to win... I see I underestimated you. But remember this, BOB NEVER LOSES!!!!")


def game_over(lives):
    """Determines whether the player has won or lost.
    
    Parameters:
        lives (value): the number of lives left
    """
    time.sleep(2.0)
    if lives==0:
        print(you_lose)
        time.sleep(2.0)
        print("All your bravery can't save you from ignorance! You have lost and Laura is forever MINE!!!!")
    else:
        print(you_win)
        time.sleep(2.0)
        print("Your may have defeated me but I'll be back! You haven't seen the last of BOB!!!")

def play():
    """
    Returns true if user inputs 'y', returns false if user inputs 'n', and prompts the user for
    a valid response if otherwise.
    
    """
    GO = ["y","n"]
    play =  input("\nThink you know more than BOB? (y/n): \n\n>>")       
    while play not in GO:
        print("\nThat is an invaild answer!\n")
        time.sleep(1.0)
        play =  input("\nDo you want to play or not? (y/n)\n")
    if play == "y":
        time.sleep(1.5)
        print("\nMuahahahaha I hoped you would say that... ")
        time.sleep(2.0)
        return True
    else:
        print(""""\n\nYou Coward! You've come all this way and don't have the guts to walk with fire! BOB will forever remain in your nightmares, and the nightmares of Twin Peaks!""")
        return False
        





def main():
    """main function to run the program, requires no objects."""
    instructions()
    if play():
        score(questions)
    print(input("Press enter key to exit: "))
        


        
        
main()



        
    
    


