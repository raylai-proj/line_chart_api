"""
Summary: linechart_helper.py generate and display line charts from Excel time-series data.

This module provides functionality to visualize time-series data from Excel sheets
as line charts. It is designed to handle files with multiple sheets, extract paired
X and Y columns, and plot each sheet with multiple Y-axes when necessary.

Functions:
- check_valid_col: Identifies valid column indices based on time-related keywords.
- remove_suffix: Cleans unit suffixes from column names when duplicated.
- draw_linechart: Reads an Excel file and plots time-series charts with dynamic Y-axes.
- generate_linechart: Prompts user to select Excel files and generates charts for each sheet.
"""

from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt
import pandas as pd

from .color import COLOR

OPENFILEFOLDEREMOJI = "\U0001f4c2"
TIME = ["time/mn", "charge time (min)"]


def check_valid_col(cols):
    """Find valid columns for plot."""
    idxs = []
    for idx, val in enumerate(cols):
        if any(word in str.lower(val) for word in TIME):
            idxs += [idx]
    return idxs


def remove_suffix(val):
    """Correct unit by remove suffix when having duplicated unit."""
    return val[:-2] if val[-2] == "." else val


def draw_linechart(file_path):
    """Draw the linechart for each sheet in excel sheet."""
    dfs = pd.read_excel(file_path, sheet_name=None)
    for key, value in dfs.items():
        cur_df = value.copy()
        # start_index = []
        cur_col = list(cur_df.columns)
        valid_cols = check_valid_col(cur_col)
        y_label_dict = dict()
        all_ylabel = dict()
        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)

        for idx, col in enumerate(valid_cols):
            x_label = cur_col[col]
            y_label = cur_col[col + 1]
            cur_x = cur_df[x_label]
            cur_y = cur_df[y_label]

            cor_y_label = remove_suffix(cur_col[col + 1])
            if idx == 0:
                ax.plot(cur_x, cur_y, color=COLOR[idx])
                ax.set_ylabel(cor_y_label, color=COLOR[idx])
                all_ylabel[cor_y_label] = True
                left_ylabel = cor_y_label
                ax.yaxis.set_tick_params()
            elif cor_y_label == left_ylabel:
                ax.plot(cur_x, cur_y, color=COLOR[idx])
            else:
                par = ax.twinx()
                par.plot(cur_x, cur_y, color=COLOR[idx])
                if cor_y_label not in all_ylabel:
                    par.set_ylabel(cor_y_label, color=COLOR[idx])
                    if y_label_dict:
                        par.spines["right"].set_position(("axes", 1.2))
                    y_label_dict[cor_y_label] = True
                    all_ylabel[cor_y_label] = True

        plt.xlabel(TIME[0])
        plt.title(key)
        plt.show()


def generate_linechart():
    """Prompt user to select files and generate line charts."""
    try:
        files = filedialog.askopenfilenames(
            title=f"Open {OPENFILEFOLDEREMOJI}",
            filetypes=[("Excel File", "*.xlsx *.xls")],
        )
        if not files:
            raise ValueError("No excel sheet selected.")
        for file in files:
            draw_linechart(file)

    except ValueError as e:
        messagebox.showwarning(title="Warning", message=e)
