import os
import random
import time
import curses

def clear_screen(stdscr):
    stdscr.clear()

def move_cursor(stdscr, a, d):
    stdscr.move(d, a)

def start_game():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)  # make getch() non-blocking

    print("Welcome to the Beat the Bug Eyes Game!\n")
    print("Press the number key that corresponds to the location of the bug eyes. 1 or 2 or 3\n")
    time.sleep(5)
    score = 0
    for _ in range(10):
        clear_screen(stdscr)
        time.sleep(random.random())  # delay for a random amount of time
        r = random.randint(1, 3)
        a = random.randint(1, curses.COLS-1)
        d = random.randint(1, curses.LINES-1)
        move_cursor(stdscr, a, d)
        stdscr.addstr("OO")
        stdscr.refresh()
        ch = stdscr.getch()
        if ch != -1:  # a key was pressed
            if ch == ord(str(r)):
                score += 1
                clear_screen(stdscr)
                move_cursor(stdscr, a, d)
                stdscr.addstr("*")
                stdscr.refresh()
                time.sleep(0.5)  # delay to make star visible
    print(f"Score: {score}")
    print("Game quit in 5s !")
    time.sleep(1)
    print(f"Score: {score}")
    print("Game quit in 4s !")
    time.sleep(1)
    print(f"Score: {score}")
    print("Game quit in 3s !")
    time.sleep(1)
    print(f"Score: {score}")
    print("Game quit in 2s !")
    time.sleep(1)
    print(f"Score: {score}")
    print("Game quit in 1s !")
    time.sleep(1)

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    start_game()