import easyocr
import cv2
import numpy as np
import docx
import os
import csv
import pandas as pd


# Creating dataset directory if does not exist
if not os.path.exists(f'{os.getcwd()}/Dataset'):
    os.mkdir(f'{os.getcwd()}/Dataset')

if not os.path.exists(f'{os.getcwd()}/temp'):
    os.mkdir(f'{os.getcwd()}/temp')


class OCR():
    def __init__(self):
        super.__init__()

    # def variables(self, d):
    #     self.detailCheck = d

    def color(self, i):
        if self.result[i][2]*100 >= 0 and self.result[i][2]*100 <= 25:
            (r, g, b) = (255, 106, 0)
        elif self.result[i][2]*100 > 25 and self.result[i][2]*100 <= 50:
            (r, g, b) = (255, 213, 0)
        elif self.result[i][2]*100 > 50 and self.result[i][2]*100 <= 75:
            (r, g, b) = (191, 255, 0)
        elif self.result[i][2]*100 > 75 and self.result[i][2]*100 <= 100:
            (r, g, b) = (85, 255, 0)
        return (b, g, r)

    def imgRead(self, fileName, model):
        # this needs to run only once to load the model into memory
        self.imG = cv2.imread(fileName)
        reader = easyocr.Reader(['en'], gpu=True, recog_network=model)
        self.result = reader.readtext(self.imG, detail=1)
        self.tempResult = []
        i = 0
        while (i < len(self.result)):
            self.tempResult.append([np.round(self.result[i][0][0]).astype(
                'int'), np.round(self.result[i][0][2]).astype('int'), self.result[i][1], self.result[i][2]])
            # word coordinates top left
            # word coordinates bottom right
            # word
            # word confidence

            i += 1

    def detailedImg(self, i, fileName):
        imgcpy = cv2.imread(fileName)
        if i == -1:
            i = 0
            for i in range(len(self.tempResult)):
                self.topLeft = self.tempResult[i][0]  # [146, 134]
                self.bottomRight = self.tempResult[i][1]  # [537, 268]

        # drawing rectanlge
                rect = cv2.rectangle(imgcpy, self.topLeft, self.bottomRight,
                                     self.color(i), thickness=2)

            if os.path.exists(f'{os.getcwd()}/temp/bound.jpg'):
                os.remove(f'{os.getcwd()}/temp/bound.jpg')
            # cv2.imshow('result', rect)
            cv2.imwrite(f'{os.getcwd()}/temp/bound.jpg', rect)

        else:
            self.topLeft = self.tempResult[i][0]  # [146, 134]
            self.bottomRight = self.tempResult[i][1]  # [537, 268]
            print(i)
        # drawing rectanlge
            rect = cv2.rectangle(imgcpy, self.topLeft,
                                 self.bottomRight, self.color(i), thickness=2)

            if os.path.exists(f'{os.getcwd()}/temp/bound.jpg'):
                os.remove(f'{os.getcwd()}/temp/bound.jpg')

            cv2.imwrite(f'{os.getcwd()}/temp/bound.jpg', rect)

    def crop_label(self, userName):

        if os.path.exists(f'{os.getcwd()}/Dataset/{userName}/labels.csv'):
            self.labels = open(f'{os.getcwd()}/Dataset/{userName}/labels.csv',
                               'r+', newline='')

            self.lastLabel = 0
            for line in csv.reader(self.labels):
                pass
            self.lastLabel = line[0]
            i = len(self.lastLabel)-1
            s = 0
            j = 0
            while (i >= 0):
                # if file is empty or there's just column names no entries
                if self.lastLabel[i].isdigit():
                    s += int(self.lastLabel[i])*(10**j)
                    j += 1
                i -= 1
            self.lastLabel = s
            self.writerObj = csv.DictWriter(self.labels, ['filename', 'words'])
        else:
            self.labels = open(
                f'{os.getcwd()}/Dataset/{userName}/labels.csv', 'a', newline='')
            self.writerObj = csv.writer(self.labels)
            self.writerObj.writerow(['filename', 'words'])
            self.writerObj = csv.DictWriter(self.labels, ['filename', 'words'])
            self.lastLabel = 0

    # def crop(self):
        for i in range(len(self.tempResult)):
            # labeling
            if self.tempResult[i][2] != '':
                self.writerObj.writerow(
                    {'filename': f'{self.lastLabel+i+1}.jpg', 'words': self.tempResult[i][2]})

                # cropping image
                self.topLeft = self.tempResult[i][0]  # [146, 134]
                self.bottomRight = self.tempResult[i][1]  # [537, 268]

                croppedImg = self.imG[self.topLeft[1]: self.bottomRight[1],
                                      self.topLeft[0]: self.bottomRight[0]]

                # saving cropped image
                cv2.imwrite(f'{os.getcwd()}/Dataset/{userName}/{self.lastLabel+i+1}.jpg',
                            croppedImg)  # f-strings

        self.labels.close()

    def docx(self, savePath):

        doc = docx.Document()
        i = 0
        while (i < len(self.tempResult)):
            if self.tempResult[i][2] != '':
                doc.add_paragraph(self.tempResult[i][2])

            i += 1

        doc.save(savePath)
