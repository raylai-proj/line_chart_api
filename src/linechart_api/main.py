import tkinter as tk

from linechart_api import utility


def main():
    window = tk.Tk()
    utility.Window(window)
    window.mainloop()


if __name__ == "__main__":
    main()
    # for idx in start_index:
    #     x_idx, y_idx = idx, idx+1
    #     x_label = cur_col[x_idx]
    #     y_label = cur_col[y_idx]
    #     x_col = cur_df.iloc[: , x_idx]
    #     y_col = cur_df.iloc[: , y_idx]
    #     print(x_label, y_label)

    # print(cur_col)
# cols = dfs.columns
# dfs = pd.read_excel("3Ah cell data sheet-SOC_vs_time_111023.xlsx", sheet_name=None, header=None)
# # print(dfs)
# for key, value in dfs.items():
#     # print(value.iloc[:,0])
#     title = value.iloc[:,0].dropna().astype("str").str.cat(sep=" ")
#     x_label = value.iloc[0, 1]
#     y_label = value.iloc[0, 2]
#     x_col = value.iloc[1:, 1]
#     y_col = value.iloc[1:, 2]
#     print(x_label, y_label)
#     print(x_col)
#     print(y_col)
#     print(title)
# print(dfs.keys())
# print("test")
