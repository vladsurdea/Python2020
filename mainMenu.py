import os
import tkinter as tink
from tkinter import *
from tkinter import Button, Label
from centerWindows import CenterWindows
import PIL.ImageTk as ImageTk
from PIL import Image


def main():
    width, height = 800, 600

    tk = tink.Tk()
    tk = CenterWindows(tk).windowsOnCenter()
    tk.title('MiniGames')   # <-- Change title here
    tk.geometry("{}x{}".format(width, height))
    tk.resizable(width=False, height=False)

    img = Image.open("fire.png").resize((width, height))

    image = ImageTk.PhotoImage(img)
    bg_label = Label(tk, image=image)
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    b1 = Button(bg_label,
                text='Fire, Fire Walk With Me',
                bg="black",
                fg="white", 
                command=lambda: start_game(tk, 'fire'))

    b1.place(relx=0.495, rely=0.65)

    b2 = Button(bg_label, 
                text='Falling Skies', 
                bg="black", 
                fg="white",
                command=lambda: start_game(tk, 'falling'))

    b2.place(relx=0.695, rely=0.65)

    b3 = Button(bg_label, 
                text='Trivia Game', 
                bg="black", 
                fg="white",
                command=lambda: start_game(tk, 'trivia'))

    b3.place(relx=0.845, rely=0.65)
    tk.mainloop()

def start_game(tk, game_name):

    tk.destroy()
    if game_name == 'fire':
        os.system('python Text-Based_Adventure_New.py')
    elif game_name == 'falling':
        os.system('python FallingSkies.py')
    elif game_name == 'trivia':
        os.system('python Trivia_Game_Update.py')

if __name__ == "__main__":
    main()