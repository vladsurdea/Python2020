# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:48:25 2020

@author: jmitc
"""
import random


QUESTION = [
    
    ("Laura's eerily similar-looking cousin is named?"," \n (a) Maddy \n (b) Donna \n (c) Kathrin\n", "a"),
    ("Dr. Jakobi hid half of Laura's necklace in a..?", " \n (a) Safe \n (b) Coconut \n (c) Old Shoe\n", "b"),
    ("James Hurley drives a..?", " \n (a) Red Corvette \n (b) Rip-Stick \n (c) Harley-Davidson\n", "c"),
    ("Agent Cooper likes his donuts filled with..?", " \n (a) Cream \n (b) Jelly \n (c) Mayonaise\n", "b"),
    ("Audrey's last name rhymes with..?", " \n (a) Scorn \n (b) Furlough  \n (c) Blitz\n", "a"),
    ("What color is Josie's lipstick?", " \n (a) Black \n (b) Red \n (c) Blue\n", "b"),
    ("How many months was Hank in jail?", " \n (a) 23 \n (b) 10 \n (c) 18\n", "c"),
    ("Pete left a fish in the percolator.","\n (T) True \n (F) False\n", "T"),
    ("Shelly concealed Leo's bloody shirt under the porch. ", "\n (T) True \n (F) False\n", "F"),
    ]

JABS = [
        ("Hah! You didn't know that one?! Nice try.\n"),
        ("You imbecile! Try again.\n"),
        ("You have answered incorrectly... One of your lives is MINE!\n"),
        ("If you want to defeat BOB you'll have to do better than that!\n"),
        ("Looks like you left your brain at home."),
        ("You are you ignorant. So bloody ignorant.")
        ]


def return_answer(prompt,option,c_answer):
    """returns true if answered correctly, false if otherwise"""
    print(prompt)
    print(option)
    answer = input("> ")
    if answer.lower() == c_answer.lower():
        print("Correct!\n")
        return True
    print(random.choice(JABS))
    return False

def main():
    lives = 3
    print("You have ", lives, "lives left. Be careful!")
    random.shuffle(QUESTION)
    for prompt,option, answer in QUESTION:
        if not return_answer(prompt,option,answer):
            lives -= 1
            if lives == 0:
                print("\nYour ignorance consigns you to oblivion!")
                return False
    print("You have completed the game! Congratulations")
    return True

main()



