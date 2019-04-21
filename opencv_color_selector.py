import cv2
import numpy as np 

# path to image
image_path = "hsv.jpg"

def createGUI():
    '''Function that creates the trackbar interface'''
    global screen, buttons
    cv2.createTrackbar("Low Hue", screen, 0,179,lambda x: updateValues(x, 0,0))
    cv2.createTrackbar("High Hue", screen, 179,179,lambda x: updateValues(x,1, 0))
    cv2.createTrackbar("Low Sat", screen, 0,255,lambda x: updateValues(x, 0,1))
    cv2.createTrackbar("High Sat", screen, 255,255,lambda x: updateValues(x, 1,1))
    cv2.createTrackbar("Low Val", screen, 0,255,lambda x: updateValues(x, 0,2))
    cv2.createTrackbar("High Val", screen, 255,255,lambda x: updateValues(x, 1,2))
    cv2.createTrackbar("Invert", screen, 0,1, doInvert)

def doInvert(val):
    '''Function that alters mask inversion'''
    global invert
    if val == 1:
        invert = True
    else:
        invert = False
    updateImg()

def updateValues(val, colrange, param):
    '''Function that updates the value ranges as set by the trackbars '''
    global col
    col[colrange][param] = val
    updateImg()

def updateImg():
    '''Displays image, masked with updated values'''
    mask = cv2.inRange(img_hsv, tuple(col[0]),tuple(col[1]))
    if invert:
        mask = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('Image', res)


### initial setup:
invert = False
screen = "Control"
cv2.namedWindow(screen, cv2.WINDOW_AUTOSIZE)
img = cv2.imread(image_path)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Image', img)
createGUI()
col = [[0,0,0],[179,255,255]]

cv2.waitKey(0)
cv2.destroyAllWindows()