import pytesseract
import cv2

def extracting(filename):
    img = cv2.imread(f"static/input/{filename}")
    extracted_text = pytesseract.image_to_string(img,lang='hin+eng')
    text = ' '.join(extracted_text.split())
    return text
