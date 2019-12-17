import sys, os
import curses
import time

def tiles(i):
    t = [0,0,1,0,0,
         0,0,0,0,0,
         0,0,0,0,0,
         0,0,0,0,0,
         1,1,0,1,1]

    for num in range(len(t)):
        if t[num] == 1:
            return 'a';

    if t[i] == 0: return '.'
    elif t[i] == 1: return '#'

def draw_menu(stdscr):
    cursor_x = 0
    cursor_y = 0

    stdscr.nodelay(1)

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    screen_height, screen_width = stdscr.getmaxyx()
    time_start = time.time()
    clock = 0

    key = ""
    bottom_line = ""

    while True:
        # inputs
        key = stdscr.getch()

        if stdscr.getch() == ord("q"):
            break

        bottom_line = "Key "+str(key)

        # collisions

        if clock != round(time.time() - time_start):
            clock = round(time.time() - time_start)
            ## DEBUG:
            stdscr.addstr(screen_height - 1, 0, str(clock))



        # draw stuff loop ##########

        #stdscr.addstr(1, 0, str(stdscr.getyx()))
        #stdscr.addstr(1, stdscr.getyx()[1], str(stdscr.getyx()))

        for x in range(25):
            stdscr.addstr(int(x/5), int(x%5), tiles(x));


        # stdscr.addstr(0, 0, tiles(t))

        # bound the cursor position
        cursor_x = max(0, cursor_x)
        cursor_x = min(screen_width - 1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(screen_height - 1, cursor_y)

        # calculate elapsed time and draw it

        # stdscr.addstr(0, 0, "Time {}".format(time_end - time_start))

        # debug zone
        #if bottom_line != "Key -1":
        #stdscr.addstr(screen_height - 1, 0, str(clock))
        #stdscr.addstr(screen_height - 1, 0, "{}".format(bottom_line))

        stdscr.refresh()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
