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
  while key.lower() == "y":
    wpmTest(stdscr)
    stdscr.addstr(2,0,"You Completed the Test! Press Y to Play again... ")
    key = stdscr.getkey()

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
  

def display_text(stdscr, target, current, wpm = 0):
  stdscr.addstr(target)
  stdscr.addstr(1,0,f"WPM: {wpm}")
  for i, char in enumerate(current): #gives element of current and index in the list
    correct_char = target[i]
    color = curses.color_pair(1)
    if char.lower() != correct_char.lower():
      color = curses.color_pair(3)
    stdscr.addstr(0,i,char, color) #this will make sure that the text will go directly over its value

def wpmTest(stdscr):
  #print target text and then user to print it 
  target_text = "Hey You Boy This is the Target Text for this text"
  current_text = []
  wpm = 0
  start_time = time.time()
  stdscr.nodelay(True) # do not delat for user to hit a key
  #Take a while loop and ask the user to type something in and everytime they type something it appears as either green or black
  while True:
    time_elapsed = max(time.time() - start_time, 1)
    wpm = round((len(current_text)/ (time_elapsed / 60)) / 5) # divide by 5 becuase average word has 5 characters 
    stdscr.erase() #clear so it doesnt keep the old text everytime
    display_text(stdscr, target_text, current_text, wpm)

    stdscr.refresh() #clears the screen after adding each time so that it doesnt make a long list of things
    if "".join(current_text).lower() == target_text.lower():
      stdscr.nodelay(False)
      break

    try:
      key = stdscr.getkey()
    except:
      time.sleep(0.02)
      continue

    if len(key)==1 and ord(key) == 27: #checks it the len of this is 1 and then it makes its so that the "BACKSPACE" is not put into ord causing a problem
      break #ord 

    if key in ("KEY_BACKSPACE", '\b' , "\x7f"):
      if len(current_text) > 0:
        current_text.pop() #will remove the last chracter of the list
    elif len(current_text) < len(target_text):
      current_text.append(key) #makes sure that if the above backspace is the case it is not being added to the text



wrapper(main)