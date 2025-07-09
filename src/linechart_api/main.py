import tkinter as tk

from linechart_api import utility


def main():
    window = tk.Tk()
    utility.Components(window)
    window.mainloop()


if __name__ == "__main__":
    main()
