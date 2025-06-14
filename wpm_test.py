import time
import keyboard
import random
import curses
from curses import wrapper

"""
Print a sentence to type.
Wait for user to press Enter to start.
Record the start time.
Accept user input.
Record end time.
Calculate WPM.
Compare to original sentence → count mistakes.
Display WPM, accuracy, and mistakes.
"""

def main(stdscr):
  stdscr.clear()
  stdscr.addstr("Hello World!")
  stdscr.refresh()
  stdscr.getkey()

wrapper(main)