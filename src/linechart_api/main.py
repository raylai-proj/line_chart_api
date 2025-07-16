"""Summary: main.py launch the main GUI window for data analysis."""

import tkinter as tk

from linechart_api import utility


def main():
    """Entry point of the program."""
    window = tk.Tk()
    utility.Components(window)
    window.mainloop()


if __name__ == "__main__":
    main()
