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

imG = cv2.imread('test case.jpg')
reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext(imG, detail=1)


# Creating document template
doc = docx.Document()

for i in range(len(result)-3):
    topLeft = result[i][0][0]  # [146, 134]
    bottomRight = result[i][0][2]  # [537, 268]
    # if type(topLeft) == list or type(bottomRight) == list:
    #     # continue
    #     list_inttl = ''
    #     list_intbr = ''
    #     for j in topLeft:
    #         list_inttl = list_inttl+str(j)
    #         list_intbr = list_intbr+str(j)
    #         topLeft = int(list_inttl)
    #         bottomRight = int(list_intbr)
    # drawing rectanlge
    rect = cv2.rectangle(imG, topLeft, bottomRight, color(i), thickness=3)
    # rect = cv2.rectangle(imG, topLeft, bottomRight, (255, 255, 0), thickness=3)

    doc.add_paragraph(result[i][1])

doc.save('result_text.docx')

cv2.imshow('result', rect)

if os.path.exists(f'{os.getcwd()}/Dataset/labels.csv'):
    labels = open(f'{os.getcwd()}/Dataset/labels.csv', 'r+', newline='')

    lastLabel = 0
    for line in csv.reader(labels):
        pass
    lastLabel = line[0]
    i = len(lastLabel)-1
    s = 0
    j = 0
    while (i >= 0):
        if lastLabel[i].isdigit():  # if file is empty or there's just column names no entries
            s += int(lastLabel[i])*(10**j)
            j += 1
        i -= 1
    lastLabel = s
    writerObj = csv.DictWriter(labels, ['filename', 'words'])
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


# cmd command to open ms word of result.docx
opt = input('Show document?(y or n)= ')

if opt == 'y':
    os.system('cmd /c "start result_text.docx"')
else:
    SystemExit()
