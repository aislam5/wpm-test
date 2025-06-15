import time
import keyboard
import random
import curses
from curses import wrapper

"""
Print a sentence to type. (Done)
Wait for user to press Enter to start.
Record the start time.
Accept user input.
Record end time.
Calculate WPM.
Compare to original sentence → count mistakes.
Display WPM, accuracy, and mistakes.
"""

def main(stdscr):
  curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # foreground color green background color is white
  curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) #The integer is the ID if 1 again it will override the existing pair 
  curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

  key = start_screen(stdscr)
  if(key.lower()!="y"):
    return
  wpmTest(stdscr)

  """stdscr.clear() #Clears the entire Screen
  stdscr.addstr(0,0,"This is the typing test and you shall not pass", curses.color_pair(1)) #Prints first number for row second foor column
  stdscr.refresh() #Need to refresh before doing anything
  key = stdscr.getkey() #This makes sure that the user types something aand then the screen goes away
  print(key)"""
  #if not in place then it will refresh super fast and we wont be able to see anything


#First Thing we will ask the user if they want to play the game and if they choose Y then play the game 
def start_screen(stdscr):
  stdscr.clear() 
  stdscr.addstr("Welcome! To the Speed Typing Test", curses.color_pair(2)) #Prints first number for row second foor column
  stdscr.addstr("\nWould You Like to Out Your Fingers to the Test Y/N: ", curses.color_pair(2))
  stdscr.refresh() 
  key = stdscr.getkey()
  return key
  
def wpmTest(stdscr):
  #print target text and then user to print it 
  target_text = "Hey You Boy This is the Target Text for this text"
  current_text = []
  stdscr.clear() 

  stdscr.addstr(target_text, curses.color_pair(2))
  stdscr.refresh()

  #Take a while loop and ask the user to type something in and everytime they type something it appears as either green or black
  while True:

    stdscr.clear() #clear so it doesnt keep the old text everytime
    stdscr.addstr(target_text)

    #loop through current_text and place the charcaters on the screen
    for char in current_text:
      stdscr.addstr(char, curses.color_pair(1))

    stdscr.refresh() #clears the screen after adding each time so that it doesnt make a long list of things
   
    key = stdscr.getkey()
    if ord(key) == 27: #ASCII REPRESENTAION OF ESCAPE KEY
      break

    if key in ("KEY_BACKSPACE"):
      if len(current_text) > 0:
        current_text.pop() #will remove the last chracter of the list
    else:
      current_text.append(key) #makes sure that if the above backspace is the case it is not being added to the text


wrapper(main)