from tkinter import ttk

from .linechart_helper import generate_linechart

ACTDICT = {
    "Generate line chart": generate_linechart,
}


class Components(object):
    def __init__(self, window):
        self.window = window
        self.label = ttk.Label(
            self.window, font=("Arial", 12), text="Select the Action:"
        )
        self.label.grid(column=0, row=0, padx=10, pady=10, sticky="e")

        self.dropdown = ttk.Combobox(
            self.window,
            font=("Arial", 12),
            values=list(ACTDICT.keys()),
            state="readonly",
        )
        self.dropdown.grid(column=1, row=0, padx=10, pady=10, sticky="w")
        self.dropdown.bind("<<ComboboxSelected>>", self.on_selection)

        self.submit_btn = ttk.Button(
            self.window, command=self.on_submit, text="Submit", state="disabled"
        )
        self.submit_btn.grid(column=0, row=2, padx=10, pady=10)

        self.exit_btn = ttk.Button(self.window, command=self.on_exit, text="Exit")
        self.exit_btn.grid(column=1, row=2, padx=10, pady=10)

    def on_selection(self, event=None):
        selection = self.dropdown.get()
        if selection:
            self.submit_btn.config(state="normal")
        else:
            self.submit_btn.config(state="disabled")

    def on_submit(self):
        act = self.dropdown.get()
        action = ACTDICT[act]
        action()

    def on_exit(self):
        self.window.quit()
