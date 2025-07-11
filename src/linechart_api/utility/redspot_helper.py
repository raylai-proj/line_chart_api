from tkinter import filedialog, messagebox

OPENFILEFOLDEREMOJI = "\U0001f4c2"


def find_hottest_region():
    """check if hottest region is distributed and find the largest hottest region"""


def process_image(file_paths):
    """analyze each images from file paths and draw arrow to point out"""


def analyze_thermo_images():
    """prompt user to select thermographic images"""
    try:
        files = filedialog.askopenfilenames(
            title=f"Open {OPENFILEFOLDEREMOJI}", filetypes=("Image Files", ".jpg .png")
        )
        if not files:
            raise ValueError("No file selected.")
        for file in list(files):
            process_image(file)
    except ValueError as e:
        messagebox.showwarning(title="Warning", message=e)
