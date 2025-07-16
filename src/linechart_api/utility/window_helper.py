"""
Summary: window_helper.py creates a GUI for selecting and executing analysis actions.

This module defines a Components class that builds a basic tkinter-based interface
with a dropdown to choose between generating line charts or analyzing thermographic images.

Features:
- Dropdown selection of analysis actions (line chart or thermal image).
- Submit and Exit buttons for executing or quitting.
- Automatic enabling/disabling of the Submit button based on user selection.

Classes:
- Components: Encapsulates the entire UI layout and event handling logic.
"""

from tkinter import ttk

from .linechart_helper import generate_linechart
from .redspot_helper import analyze_thermo_images

ACTDICT = {
    "Generate line chart": generate_linechart,
    "Analyze thermo image": analyze_thermo_images,
}
FONT = ("Arial", 12)
PAD = 10


class Components(object):
    """Components class create a window to provide actions in daily task."""

    def __init__(self, window):
        """Initialize Components object and creating a window for daily task simulation."""
        self.window = window
        self.label = ttk.Label(self.window, font=FONT, text="Select the Action:")
        self.label.grid(column=0, row=0, padx=PAD, pady=PAD, sticky="e")

        self.submit_btn = ttk.Button(
            self.window, command=self.on_submit, text="Submit", state="disabled"
        )
        self.submit_btn.grid(column=0, row=2, padx=PAD, pady=PAD)

        self.exit_btn = ttk.Button(self.window, command=self.on_exit, text="Exit")
        self.exit_btn.grid(column=1, row=2, padx=PAD, pady=PAD)

        self.dropdown = ttk.Combobox(
            self.window,
            font=FONT,
            values=list(ACTDICT.keys()),
            state="readonly",
        )
        self.dropdown.grid(column=1, row=0, padx=PAD, pady=PAD, sticky="w")
        self.dropdown.bind(
            "<<ComboboxSelected>>",
            lambda event: self.submit_btn.config(
                state="normal" if self.dropdown.get() else "disabled"
            ),
        )

    def on_submit(self):
        """Execute function when clicking on_submit."""
        ACTDICT[self.dropdown.get()]()

    def on_exit(self):
        """Quit window when clicking on_exit."""
        self.window.quit()
