# Made by marquis-ng

import curses

class Item:
    def __init__(self, disp, real):
        self.disp = disp
        self.real = real

def main(stdscr):
    stdscr.keypad(True)
    curses.curs_set(False)

    blocko = ["System", "Time", "Status","Shell", "Command", "Colors", "Styles","Characters", "Reset"]
    blocks = {"System": [
        Item("user", "\\u"),
        Item("host (short)", "\\h"),
        Item("host", "\\H"),
    ], "Time": [
        Item("date", "\\d"),
        Item("am/pm", "\\@"),
        Item("24 hr", "\\A"),
        Item("12 hr (secs.)", "\\T"),
        Item("24 hr (secs.)", "\\t"),
    ], "Status": [
        Item("cwd", "\\w"),
        Item("cwd (base)", "\\W"),
        Item("root status", "\\$")
    ], "Shell": [
        Item("bash ver. (short)", "\\v"),
        Item("bash ver.", "\\V"),
        Item("tty", "\\l"),
        Item("shell", "\\s")
    ], "Command": [
        Item("history no.", "\\!"),
        Item("command no.", "\\#"),
        Item("jobs", "\\j")
    ], "Colors": [
        Item("red", "\\[\\033[31m\\]"),
        Item("green", "\\[\\033[32m\\]"),
        Item("yellow", "\\[\\033[33m\\]"),
        Item("blue", "\\[\\033[34m\\]"),
        Item("magenta", "\\[\\033[35m\\]"),
        Item("cyan", "\\[\\033[36m\\]"),
    ], "Styles": [
        Item("bold", "\\[\\033[1m\\]"),
        Item("dim", "\\[\\033[2m\\]"),
        Item("italic", "\\[\\033[3m\\]"),
        Item("underline", "\\[\\033[4m\\]"),
        Item("blink", "\\[\\033[5m\\]"),
        Item("reverse", "\\[\\033[7m\\]"),
    ], "Characters": [
        Item("\\n", "\\n"),
        Item(":", ":"),
        Item("[", "["),
        Item("]", "]"),
        Item("-", "-"),
        Item("@", "@"),
        Item("space", " ")
    ], "Reset": [
        Item("reset all", "\\[\\033[0m\\]")
    ]}

    items = []
    cursx = 0
    cursy = 0
    lastx = 0

    while True:
        stdscr.erase()
        stdscr.addstr("PS1 generator\n\n", curses.A_BOLD | curses.A_UNDERLINE | curses.A_REVERSE)
        stdscr.addstr("Items:\n", curses.A_BOLD)
        stdscr.addstr("-" * (stdscr.getmaxyx()[1]))
        stdscr.addstr(" ".join([f"[{i.disp}]" for i in items])[1 - stdscr.getmaxyx()[1]:])
        stdscr.addstr(f"\n{'-' * (stdscr.getmaxyx()[1])}\n")

        for idxy, block in enumerate(blocko):
            stdscr.addstr(f"{block}: ", curses.A_BOLD)
            for idxx, item in enumerate(blocks[block]):
                stdscr.addstr(f"[{item.disp}]" , curses.A_REVERSE if idxx == cursx and idxy == cursy else curses.A_NORMAL)
                stdscr.addstr("\n" if idxx == len(blocks[block]) - 1 else " ")
        stdscr.refresh()

        key = stdscr.getkey()
        if key == "KEY_UP":
            cursy -= 1
            cursx = lastx

        elif key == "KEY_DOWN":
            cursy += 1
            cursx = lastx

        elif key == "KEY_LEFT":
            cursx -= 1
            lastx = cursx
            
        elif key == "KEY_RIGHT":
            cursx += 1
            lastx = cursx

        elif key == "KEY_HOME":
            cursx = 0
            lastx = cursx

        elif key == "KEY_END":
            cursx = len(blocks[blocko[cursy]]) - 1
            lastx = cursx

        elif key in ("\n", " "):
            items.append(blocks[blocko[cursy]][cursx])

        elif key == "\x7f":
            if len(items) > 0:
                del items[-1]
            else:
                curses.beep()

        elif key in ("q", "Q"):
            return items

        if cursy < 0:
            cursy = len(blocko) - 1
        elif cursy > len(blocko) - 1:
            cursy = 0

        if cursx < 0:
            cursx = len(blocks[blocko[cursy]]) - 1
        elif cursx > len(blocks[blocko[cursy]]) - 1:
            if key in ("KEY_UP", "KEY_DOWN"):
                cursx = len(blocks[blocko[cursy]]) - 1
            else:
                cursx = 0

try:
    print(f"export PS1=\"{''.join([i.real for i in curses.wrapper(main)])}\"")
except BaseException:
    pass
