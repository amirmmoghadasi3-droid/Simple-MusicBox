"""
Controls:
  s / Down arrow  -> move down
  w / Up arrow    -> move up
  Enter           -> select
  q               -> quit

"""
import curses


def Open_folder(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 2, "You selected: Open folder  (press any key to go back)")
    stdscr.refresh()
    stdscr.getch()


def Show_playlist(stdscr, playlist: list):

    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "=== PLAYLIST ===\n")

        for i, music_name in enumerate(playlist):
            marker = "> " if i == selected else "  "
            line = f"{marker}{music_name}"
            if i == selected:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(i + 2, 2, line)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 2, line)

        stdscr.refresh()

        key = stdscr.getch()
        if key in (ord('s'), ord('S'), curses.KEY_DOWN):
            selected = (selected + 1) % len(playlist)
        elif key in (ord('w'), ord('W'), curses.KEY_UP):
            selected = (selected - 1) % len(playlist)
        elif key in (curses.KEY_ENTER, 10, 13):
            return music_name


def Search(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 2, "You selected: search  (press any key to go back)")
    stdscr.refresh()
    stdscr.getch()


def Setting_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 2, "You selected: setting  (press any key to go back)")
    stdscr.refresh()
    stdscr.getch()


def Main_menu(stdscr, audio_files: list):
    curses.curs_set(0)      # hide the blinking cursor
    stdscr.keypad(True)     # decode arrow keys into curses constants

    options = ["Open folder", "Playlist", "Search", "Settings", "Quit"]
    selected = 0
    music_name = None

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "Simple-MusicBox  (W/S or arrows to move, Enter to select, q to quit)")

        for i, opt in enumerate(options):
            marker = "> " if i == selected else "  "
            line = f"{marker}{opt}"
            if i == selected:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(i + 2, 2, line)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 2, line)

        stdscr.refresh()

        key = stdscr.getch()  # blocks until a key is pressed

        if key in (ord('s'), ord('S'), curses.KEY_DOWN):
            selected = (selected + 1) % len(options)
        elif key in (ord('w'), ord('W'), curses.KEY_UP):
            selected = (selected - 1) % len(options)
        elif key in (curses.KEY_ENTER, 10, 13):
            if options[selected] == "Quit":
                break

            match options[selected]:
                case "Open folder": Open_folder(stdscr)
                case "Playlist": music_name = Show_playlist(stdscr, audio_files)
                case "Search": Search(stdscr)
                case "Settings": Setting_menu(stdscr)

            if music_name != None:
                return music_name
            
        elif key == ord('q') or key == ord('Q'):
            break
    return


if __name__ == "__main__":
    test_files = ['test1.mp3', 'test2.wav', 'test3.mp3']
    curses.wrapper(Main_menu, test_files)
