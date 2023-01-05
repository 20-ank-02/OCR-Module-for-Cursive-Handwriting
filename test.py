import easyocr
import cv2
import numpy as np
import docx
import os
import csv
import pandas as pd
# Creating dataset directory if does not exist
if not os.path.exists('Dataset'):
    os.mkdir('Dataset')


def color(i):
    if result[i][2]*100 >= 0 and result[i][2]*100 <= 25:
        (r, g, b) = (255, 106, 0)
    elif result[i][2]*100 > 25 and result[i][2]*100 <= 50:
        (r, g, b) = (255, 213, 0)
    elif result[i][2]*100 > 50 and result[i][2]*100 <= 75:
        (r, g, b) = (191, 255, 0)
    elif result[i][2]*100 > 75 and result[i][2]*100 <= 100:
        (r, g, b) = (85, 255, 0)
    return (b, g, r)


# this needs to run only once to load the model into memory
# , recog_network='best_accuracy'

imG = cv2.imread('test case.jpg')
reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext(imG, detail=1)

# for this image, result is a list containing 2 tuples. each for detected text
# tuples contain (Coordinates,Text,Confidence)
#result=[([[146, 134], [537, 134], [537, 268], [146, 268]], 'Sample', 0.9549119391612874), ([[442, 400], [516, 400], [516, 430], [442, 430]], ' ;', 0.1835381164882384)]
# coordinates are line start and end points
# cv2.line(image, start_point, end_point, color, thickness)
# ([[top left-x,y],top right[x,y],bottom right[x,y],bottom left-[x,y]],'Sample',0.9549119391612874)

# 4th quadrant
# 0--------------255
# |TL        TR
# |
# |
# |BL        BR
# 255
# line = cv2.line(imG, (146, 134), (537, 134), (255, 0, 0), 3)
# cv2.imshow('result', line)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()

# Creating document template
doc = docx.Document()

for i in range(len(result)-3):
    topLeft = result[i][0][0]  # [146, 134]
    bottomRight = result[i][0][2]  # [537, 268]

    # drawing rectanlge
    rect = cv2.rectangle(imG, topLeft,
                         bottomRight, color(i), thickness=3)

    doc.add_paragraph(result[i][1])

doc.save('result_text.docx')

cv2.imshow('result', rect)

if os.path.exists(f'{os.getcwd()}/Dataset/labels.csv'):
    labels = open(f'{os.getcwd()}/Dataset/labels.csv', 'r+', newline='')
    # code for, if file is empty or there's just column names no entries
    lastLabel = csv.reader(labels)[-1]
    i = len(lastLabel[0])-5
    s = 0
    while (i >= 0):
        s += int(lastLabel[0][i])*(10**((len(lastLabel[0])-5)-i))
        i -= 1
    lastLabel = s
else:
    labels = open(f'{os.getcwd()}/Dataset/labels.csv', 'a', newline='')
    writerObj = csv.writer(labels)
    writerObj.writerow(['filename', 'words'])
    writerObj = csv.DictWriter(labels, ['filename', 'words'])
    lastLabel = 0


# # caputering pressed key
k = cv2.waitKey(0)

if k == 27:
    for i in range(len(result)-3):
        # labeling
        writerObj.writerow(
            {'filename': f'{lastLabel+i+1}.jpg', 'words': result[i][1]})

        # cropping image
        # roi = image[startY:endY, startX:endX]
        # https://pyimagesearch.com/2021/01/19/crop-image-with-opencv/
        topLeft = result[i][0][0]
        bottomRight = result[i][0][2]

        croppedImg = imG[topLeft[1]: bottomRight[1],
                         topLeft[0]: bottomRight[0]]

        # saving cropped image
        cv2.imwrite(f'{os.getcwd()}/Dataset/{lastLabel+i+1}.jpg',
                    croppedImg)  # f-strings


# closing all opened windows and files
cv2.destroyAllWindows()
labels.close()

# Once in the directory containing the document, use the start command to start the document in Windows.
# For example, if the document is called "example.doc," you would type the following command.
# start example.doc


# -------------Cmd Command execution---------------
# (1) CMD /K – execute a command and then remain:
# import os
# os.system('cmd /k "Your Command Prompt Command"')

# (2) CMD /C – execute a command and then terminate:

# import os
# os.system('cmd /c "Your Command Prompt Command"')

opt = input('Show document?(y or n)= ')

if opt == 'y':
    os.system('cmd /c "start result_text.docx"')
else:
    SystemExit()
