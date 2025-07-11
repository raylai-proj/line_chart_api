from tkinter import filedialog, messagebox

import cv2
import matplotlib.pyplot as plt
import numpy as np

OPENFILEFOLDEREMOJI = "\U0001f4c2"
DPI = 100


def find_hottest_spot(color_img):
    """check if hottest region is distributed and find the largest hottest region"""
    # convert from BGR to gray scale
    gray_img = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY)
    # use gaussian blur to smooth the grayscale image
    blur_img = cv2.GaussianBlur(gray_img, ksize=(11, 11), sigmaX=0)
    # get max_val from image matrix
    max_val = np.max(blur_img)
    # set threshold to pick hottest spot over 98%
    _, hot_mask = cv2.threshold(
        blur_img, thresh=max_val * 0.98, maxval=255, type=cv2.THRESH_BINARY
    )
    hot_mask = hot_mask.astype(np.uint8)
    # find the contours of hot regions
    contours, _ = cv2.findContours(
        hot_mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE
    )
    # find the largest contour region aka. largest hotspot region
    if not contours:
        raise Exception("No hot region found in image")
    max_contour = max(contours, key=cv2.contourArea)
    # find the centroid using cv2.moments
    m_dict = cv2.moments(max_contour)
    if m_dict["m00"] == 0:
        raise Exception("Couldn't detect largest contour")
    # m_dict["m00"]: are, m_dict["m10"]: sum of x-coordinates, m_dict["m01"]: sum of y-coordinates
    # m_dict["m10"]/m_dict["m00"]: avg. x, m_dict["m01"]/m_dict["m00"]: avg. y
    return int(m_dict["m10"] / m_dict["m00"]), int(m_dict["m01"] / m_dict["m00"])


def process_image(file_path):
    """analyze each images from file paths and draw arrow to point out"""
    try:
        color_img = cv2.imread(file_path)
        if color_img is None:
            raise Exception(f"Unable to read file: {color_img}")
        cx, cy = find_hottest_spot(color_img)

        # draw the line to point hottest centroid
        annotated_img = color_img.copy()

        height, width = annotated_img.shape[:2]
        cv2.arrowedLine(
            annotated_img,
            pt1=(cx + (height // 15), cy - (width // 15)),
            pt2=(cx, cy),
            color=(0, 0, 255),
            thickness=7,
            tipLength=0.4,
        )

        annotated_rgb = cv2.cvtColor(src=annotated_img, code=cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(height / DPI, width / DPI), dpi=DPI)
        plt.imshow(annotated_rgb)
        plt.axis("off")
        plt.show()
    except Exception as e:
        raise Exception(e)


def analyze_thermo_images():
    """prompt user to select thermographic images"""
    try:
        files = filedialog.askopenfilenames(
            title=f"Open {OPENFILEFOLDEREMOJI}",
            filetypes=[("Image File", "*.jpg *.jpeg"), ("Image File", "*.png")],
        )
        if not files:
            raise ValueError("No file selected.")
        for file in list(files):
            process_image(file)
    except ValueError as e:
        messagebox.showwarning(title="Warning", message=e)
