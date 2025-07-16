from tkinter import filedialog, messagebox

import cv2
import matplotlib.pyplot as plt
import numpy as np

OPENFILEFOLDEREMOJI = "\U0001f4c2"
DPI = 100

RED_HSV = {
    "lower_red1": [0, 100, 100],
    "upper_red1": [10, 255, 255],
    "lower_red2": [160, 100, 100],
    "upper_red2": [180, 255, 255],
}


def find_hottest_contour(color_img):
    """check if hottest region is distributed and find the largest hottest region"""
    # convert from BGR to gray scale
    gray_img = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY)
    # use gaussian blur to smooth the grayscale image
    blur_img = cv2.GaussianBlur(gray_img, ksize=(11, 11), sigmaX=0)
    # get max_val from image matrix
    max_val = np.max(blur_img)
    # set threshold to pick hottest spot over 98%
    _, hot_mask = cv2.threshold(
        blur_img, thresh=max_val * 0.8, maxval=255, type=cv2.THRESH_BINARY
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
    return max_contour


def find_reddest_contour(color_img):
    """find the reddest contour"""
    hsv_img = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2HSV)
    # define HSV ranges for red
    lower_red1, upper_red1 = np.array(RED_HSV["lower_red1"]), np.array(
        RED_HSV["upper_red1"]
    )
    lower_red2, upper_red2 = np.array(RED_HSV["lower_red2"]), np.array(
        RED_HSV["upper_red2"]
    )

    # create red_mask based on HSV red stanard
    mask1 = cv2.inRange(hsv_img, lowerb=lower_red1, upperb=upper_red1)
    mask2 = cv2.inRange(hsv_img, lowerb=lower_red2, upperb=upper_red2)
    red_mask = cv2.bitwise_or(src1=mask1, src2=mask2)

    # find the contours of hot regions
    contours, _ = cv2.findContours(
        image=red_mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE
    )
    # find the largest contour region aka. largest reddest region
    if not contours:
        raise Exception("No red region found in image")
    return max(contours, key=cv2.contourArea)


def find_centroid(contour):
    # find the centroid using cv2.moments
    m_dict = cv2.moments(contour)
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
        # # preserve find most intense contour for the future reference
        # max_contour = find_hottest_contour(color_img)
        max_contour = find_reddest_contour(color_img)
        cx, cy = find_centroid(max_contour)
        # draw the line to point hottest centroid
        annotated_img = color_img.copy()
        # # testing find the correct contour
        # cv2.drawContours(
        #     image=annotated_img,
        #     contours=[max_contour],
        #     contourIdx=-1,
        #     color=(255, 255, 255),
        #     thickness=3,
        # )

        height, width = annotated_img.shape[:2]
        cv2.arrowedLine(
            annotated_img,
            pt1=(cx + (height // 15), cy - (width // 15)),
            pt2=(cx, cy),
            color=(255, 255, 255),
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
            filetypes=[("Image File", "*.jpg *.jpeg *.png")],
        )
        if not files:
            raise ValueError("No file selected.")
        for file in list(files):
            process_image(file)
    except ValueError as e:
        messagebox.showwarning(title="Warning", message=e)
