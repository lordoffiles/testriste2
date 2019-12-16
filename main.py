import sys, os
import curses
import time

t = [0,1,1,1,0,
     0,0,1,0,0]

def tiles(t):
    o = ''
    for x in t:
        if t[x] == 0: o += '.'
        elif t[x] == 1: o += '#'
    return o

def draw_menu(stdscr):
    cursor_x = 0
    cursor_y = 0

    stdscr.nodelay(1)

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    screen_height, screen_width = stdscr.getmaxyx()
    time_start = time.time()

    key = ""
    bottom_line = ""

    while True:
        # inputs
        key = stdscr.getch()

        if stdscr.getch() == ord("q"):
            break

        bottom_line = "Key "+str(key)

        # collisions

        # draw stuff loop ##########

        stdscr.addstr(1, 0, str(stdscr.getyx()))
        stdscr.addstr(1, stdscr.getyx()[1], str(stdscr.getyx()))

        # stdscr.addstr(0, 0, tiles(t))

        # bound the cursor position
        cursor_x = max(0, cursor_x)
        cursor_x = min(screen_width - 1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(screen_height - 1, cursor_y)

        # calculate elapsed time and draw it
        time_end = time.time()
        stdscr.addstr(0, 0, "Time {}".format(round(time_end - time_start)))

        # debug zone
        if bottom_line != "Key -1":
            stdscr.addstr(screen_height - 1, 0, "".join([" " for i in range(screen_width - 1)]))
            stdscr.addstr(screen_height - 1, 0, "{}".format(bottom_line))

        stdscr.refresh()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
