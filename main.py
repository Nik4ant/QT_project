import sys
import os

from ui import login_form, board_selection


def main():
    # Using append is good practise
    # (Because insert can overload the standard python behavior)
    sys.path.append(os.curdir)
    # If return value is True we need to open board selection menu
    user_id, need_to_open = login_form.start()
    if need_to_open:
        board_selection.start(user_id[0])


if __name__ == '__main__':
    main()
