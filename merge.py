import cv2
import os
def image1(filename):
    file1 = filename
    file2 = "bg.jpeg"
    folder_path = "static/input"
    file1_path=os.path.join(folder_path,file1)
    file2_path=os.path.join(folder_path,file2)
    os.rename(file1_path,file2_path)

def image2(filename):
    file1 = filename
    file2 = "fg.jpeg"
    folder_path = "static/input"
    file1_path=os.path.join(folder_path,file1)
    file2_path=os.path.join(folder_path,file2)
    os.rename(file1_path,file2_path)

def merger():
    bg = cv2.imread("static/input/bg.jpeg", cv2.IMREAD_COLOR)
    fg = cv2.imread("static/input/fg.jpeg", cv2.IMREAD_COLOR)
    dim = (1200, 800)
    resized_bg = cv2.resize(bg, dim, interpolation = cv2.INTER_AREA)
    resized_fg = cv2.resize(fg, dim, interpolation = cv2.INTER_AREA)
    # blend = (image scr1)*(src1 weight) + (image scr2)*(src2 weight) + gamma
    merge = cv2.addWeighted(resized_bg, 0.5, resized_fg, 0.8, 0.0)
    cv2.imwrite(f"static/output/merged.jpeg", merge)