import cv2

def converter(filename):
    image = cv2.imread(f"uploads/{filename}")
    newimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # adaptiveimage = cv2.adaptiveThreshold(newimage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,41,5)
    cv2.imwrite(f"static/{filename}", newimage)
    # cv2.imwrite(f"test/{filename}", adaptiveimage)
    
