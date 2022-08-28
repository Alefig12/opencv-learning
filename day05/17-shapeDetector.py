import cv2
import numpy as np


def getShapeName(approx):

    if len(approx) == 3:
        return 'triangle'
    elif len(approx) == 4:
        aspectRatio = float(w)/h
        if aspectRatio > 0.92 and aspectRatio < 1.09:
            return 'square'
        else:
            return 'rectangle'
    else:
        return 'circle'


def getColor(maskhsv, colors):

    for c in colors:
        mask = getColorMask(maskhsv, colors[c])
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[1]
        if cnts is not None and len(cnts) > 0:
            return colors[c]['name']


def getColorMask(hsv, color):
    lower = color['lower']
    upper = color['upper']

    mask = cv2.inRange(hsv, lower, upper)

    if (color['name'] == 'red'):
        lower2 = color['lower2']
        upper2 = color['upper2']
        mask2 = cv2.inRange(hsv, lower2, upper2)

        mask = cv2.add(mask, mask2)

    return mask


colors = {
    'blue': {
        'lower': np.array([90, 50, 20], dtype=np.uint8),
        'upper': np.array([124, 255, 255], dtype=np.uint8),
        'name': 'Blue'
    },

    'yellow': {
        'lower': np.array([20, 50, 20], dtype=np.uint8),
        'upper': np.array([40, 255, 255], dtype=np.uint8),
        'name': 'Yellow'
    },

    'green': {
        'lower': np.array([45, 85, 20], dtype=np.uint8),
        'upper': np.array([77, 255, 255], dtype=np.uint8),
        'name': 'Green'
    },

    'red': {
        'lower': np.array([1, 20, 50], dtype=np.uint8),
        'upper': np.array([10, 255, 255], dtype=np.uint8),
        'lower2': np.array([170, 20, 50], dtype=np.uint8),
        'upper2': np.array([179, 255, 255], dtype=np.uint8),
        'name': 'Red'
    },
    'purple': {
        'lower': np.array([130, 50, 20], dtype=np.uint8),
        'upper': np.array([150, 255, 255], dtype=np.uint8),
        'name': 'Purple'
    },
}


img = cv2.imread(r'input_assets\figures.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY_INV)[1]
thresh = cv2.dilate(thresh, None, iterations=1)
thresh = cv2.erode(thresh, None, iterations=1)

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

for c in cnts:
    epsilon = 0.012*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    x, y, w, h = cv2.boundingRect(approx)

    aux = np.zeros(img.shape[:2], dtype=np.uint8)

    aux = cv2.drawContours(aux, [c], -1, 255, -1)

    maskhsv = cv2.bitwise_and(hsv, hsv, mask=aux)

    print(maskhsv.shape)
    color = getColor(maskhsv, colors)
    shape = getShapeName(approx)

    cv2.putText(img, '{} {}'.format(color, shape),
                (x, y-5), 1, 1, (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)
