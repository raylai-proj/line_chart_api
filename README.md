# line_chart_api <br >
This is a comprehensive project that provide daily work simulation. <br >
The project allow users to quickly generate results of their laboratory work. <br >
The development of this project is refer to following webpages: <br >
The project has several functional components and will be introduced sequentially. <br >

## The Window layout:
The window layout class development utilized library: tkinter, tkinter.ttk, and ttk.py apis: label, button, combobox.<br >
The class development was refer to the following websites and chatGPT: <br >
1. tkinter — Python interface to Tcl/Tk: https://docs.python.org/3/library/tkinter.html<br >
2. TkDocs-Basic Widgets: https://tkdocs.com/tutorial/widgets.html#combobox<br >
3. Multiple root windows with Tkinter: https://www.reddit.com/r/learnpython/comments/51ry80/multiple_root_windows_with_tkinter/<br >
4. Python Tkinter Button Docs – TutorialsPoint: https://www.tutorialspoint.com/python/tk_button.htm<br >
5. Tkinter Combobox Reference: https://docs.python.org/3/library/tkinter.ttk.html#combobox<br >
6. TkDocs-The Grid Geometry Manager: https://tkdocs.com/tutorial/grid.html<br >
7. Combobox Widget in tkinter | Python: https://www.geeksforgeeks.org/python/combobox-widget-in-tkinter-python/<br >
8. GUI > Event-Driven Programming > tkinter Main Loop: https://textbooks.cs.ksu.edu/cc410/ii-gui/13-event-driven-programming/07-tkinter-main-loop/<br >
9. How to use a <ComboboxSelected> virtual event with tkinter: https://stackoverflow.com/questions/40641130/how-to-use-a-comboboxselected-virtual-event-with-tkinter <br >
10. tkinter: How do I make it so if I select an option from a dropdown, it will disable specific Entry boxes?: https://stackoverflow.com/questions/66980541/tkinter-how-do-i-make-it-so-if-i-select-an-option-from-a-dropdown-it-will-disa<br >
11. TkDocs-Event handling:https://tkdocs.com/tutorial/concepts.html#events<br >
12. What is the difference between root.destroy() and root.quit()?: https://stackoverflow.com/questions/2307464/what-is-the-difference-between-root-destroy-and-root-quit<br >
13. What are Namespace Packages?: https://www.tutorialspoint.com/how-to-import-everything-from-a-python-namespace-package <br >
14. tkinter.ttk — Tk themed widgets: https://docs.python.org/3/library/tkinter.ttk.html<br >

## Lessons learned when developing window layout:
1. What is namespace in python: <br >
In Python, a namespace is like a labeled box where names (like variables, functions, classes) are stored. When saying `import tkinter as tk`, it basically means <br >
> Import everything from tkinter module and store it in a box called "tk" <br >

2. Since `ttk.py` and `__init__.py` both in tkinter/, if I import tkinter as tk, why it doesn't import ttk as well: <br >
> Even though both `__init__.py` and `ttk.py` are in tkinter/ package, `import tkinter as tk` will only import `__init__.py` and no other submodule like `ttk.py`. To use `ttk.py`, we have to import it explicitly, such as `from tkinter import ttk`<br >
