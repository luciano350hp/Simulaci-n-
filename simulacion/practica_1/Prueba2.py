#!/usr/bin/env python
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        try:
            stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
        except ZeroDivisionError:
            stdscr.addstr(i,0,'10 divided by {} is {}'.format(v,"Macri Gato"))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
