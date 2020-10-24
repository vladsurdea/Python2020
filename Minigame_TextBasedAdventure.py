import sys, random, time
from os import system

def c(): system('clear')


class Room():
  def __init__(self): pass
  def play(self):
    print('This room hasnt been initialized yet.')
    
    
class Win(Room):
  def play(self):
    time.sleep(5)
    a = [
      'You live on to see another day!',
      'You are alive for know, keep up the good work.',
    ]
    print(random.choice(a))
    time.sleep(3)
    print('Game Over!')
    sys.exit()

    
class Game_Over(Room):
  def play(self):
    time.sleep(5)
    a = [
      'The mystery continues without you.',
      'Now, you may never leaver the Black Lodge',
      'Welcome to an eternity in the Lodge'
    ]
    print(random.choice(a))
    time.sleep(3)
    print('Game Over!')
    sys.exit()
    
    
    
class Intro(Room):
  def play(self):
    c()
    print('Welcome To The First Game.')
    if not input('Ready? [y/n]: ') == 'y': sys.exit()
    c()
    print('Choice 1')
    o = input('Move? [1, 2, 3]: ')
    c()
    if o == '1':
        print("X")
        return 'game over'
    elif o == '2':
        print("Y")
        return 'corridor'
    elif o == '3':
        print("Z")
        return 'game over'
  


class Intro(Room):
  def play(self):
    c()
    
class Lodge(Room):
  def play(self):
    c()
    
class Bob(Room):
  def play(self):
    c()
    
class Bridge(Room):
  def play(self):
    c()
    
class EscapeRoom(Room):
  def play(self):
    c()
    
    
engine = {
  'game over': Game_Over(),
  'intro': Intro(),
  'lodge': Lodge(),
  'bob': bob(),
  'bridge': Bridge(),
  'forre': EscapeRoom(),
  'win': Win()
}
