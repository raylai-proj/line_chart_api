from tkinter import ttk

from .linechart_helper import generate_linechart

ACTDICT = {
    "Generate line chart": generate_linechart,
}
FONT = ("Arial", 12)
PAD = 10


class Components(object):
    def __init__(self, window):
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
        ACTDICT[self.dropdown.get()]()

    def on_exit(self):
        self.window.quit()
