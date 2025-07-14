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

## Lessons learned when developing window layout:<br >
1. What is namespace in python: <br >
In Python, a namespace is like a labeled box where names (like variables, functions, classes) are stored. When saying `import tkinter as tk`, it basically means <br >
> Import everything from tkinter module and store it in a box called "tk" <br >

2. Since `ttk.py` and `__init__.py` both in tkinter/, if I import tkinter as tk, why it doesn't import ttk as well: <br >
> Even though both `__init__.py` and `ttk.py` are in tkinter/ package, `import tkinter as tk` will only import `__init__.py` and no other submodule like `ttk.py`. To use `ttk.py`, we have to import it explicitly, such as `from tkinter import ttk`<br >

## Analyze thermal image:<br >
The analyze thermal image accepts thermographic photos (expect to rainbow color-to-temperature mapping) and draw an arrow to point out the centroid of the reddest spot. The user can select `Analyze thermal image` from dropdown menu in the window. After clicking `Submit`, the image analyzer will open a window to prompt user select 1-to-multiple photos (can be *.jpg, *jpeg, or *png) and analyze each photo to find the centroid of the reddest spot in it. The image analyzer will then draw a white arrow to point out the centroid of the reddest spot and display the photos sequentially to the user, and the user can save the the photo by pressing the "save the figure" icon.<br >
The development of thermal image analyzer was referred as following website and chatGPT:<br >
1. OpenCV - Imaging file reading and writing - imread(): https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 <br >
2. Detecting warm colors in the Python image: https://stackoverflow.com/questions/61599703/detecting-warm-colors-in-the-python-image<br >
3. OpenCV - Basic Operations on Images: https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html<br >
4. matplotlib.pyplot.figure(): https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html<br >
5. OpenCV - Contour Detection using OpenCV (Python/C++): https://learnopencv.com/contour-detection-using-opencv-python-c/<br >
6. OpenCV - Image Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
7. OpenCV - Contour: Getting Started: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html<br >
8. OpenCV - Image Moments: https://docs.opencv.org/3.4/d0/d49/tutorial_moments.html<br >
9. OpenCV - Smoothing Images: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html<bt >
10. geeksforgeeks - Python OpenCV | cv2.arrowedLine() method: https://www.geeksforgeeks.org/python/python-opencv-cv2-arrowedline-method/<br >
11. pyimagesearch - Finding the Brightest Spot in an Image Using Python and OpenCV: https://pyimagesearch.com/2014/09/29/finding-brightest-spot-image-using-python-opencv/<br >
12. geeksforgeeks - Python OpenCV | cv2.cvtColor() method: https://www.geeksforgeeks.org/python/python-opencv-cv2-cvtcolor-method/<br >
13. Numpy - Indexing on ndarrays: https://numpy.org/doc/stable/user/basics.indexing.html#boolean-or-mask-index-arrays<br >
14. geeksforgeeks - cv2.imread() method - Python OpenCV:　https://www.geeksforgeeks.org/python/python-opencv-cv2-imread-method/<br >
15. Find and Draw Contours using OpenCV - Python: https://www.geeksforgeeks.org/python/find-and-draw-contours-using-opencv-python/<br >
16. numpy.zeros_like: https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html<br >
