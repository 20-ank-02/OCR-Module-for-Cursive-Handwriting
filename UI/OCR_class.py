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
        self.tempResult = ''
        i = 0
        while (i < len(self.result)):
            self.tempResult += f'{self.result[i][1]}_,_'
            i += 1

    def detailedImg(self):
        for i in range(len(self.result)):
            self.topLeft = np.round(
                self.result[i][0][0]).astype('int')  # [146, 134]
            self.bottomRight = np.round(
                self.result[i][0][2]).astype('int')  # [537, 268]
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
            rect = cv2.rectangle(self.imG, self.topLeft, self.bottomRight,
                                 self.color(i), thickness=3)

        # cv2.imshow('result', rect)
        cv2.imwrite(f'{os.getcwd()}/temp/bound.jpg', rect)

    def crop_label(self):

        if os.path.exists(f'{os.getcwd()}/Dataset/labels.csv'):
            self.labels = open(f'{os.getcwd()}/Dataset/labels.csv',
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
                f'{os.getcwd()}/Dataset/labels.csv', 'a', newline='')
            self.writerObj = csv.writer(self.labels)
            self.writerObj.writerow(['filename', 'words'])
            self.writerObj = csv.DictWriter(self.labels, ['filename', 'words'])
            self.lastLabel = 0

    # def crop(self):
        for i in range(len(self.result)):
            # labeling
            self.writerObj.writerow(
                {'filename': f'{self.lastLabel+i+1}.jpg', 'words': self.correctResult[i]})

            # cropping image
            self.topLeft = np.round(self.result[i][0][0]).astype(int)
            self.bottomRight = np.round(self.result[i][0][2]).astype(int)

            croppedImg = self.imG[self.topLeft[1]: self.bottomRight[1],
                                  self.topLeft[0]: self.bottomRight[0]]

            # saving cropped image
            cv2.imwrite(f'{os.getcwd()}/Dataset/{self.lastLabel+i+1}.jpg',
                        croppedImg)  # f-strings

        self.labels.close()

    def docx(self, savePath):

        self.correctResult = self.tempResult.split(sep='_,_')
        doc = docx.Document()
        i = 0
        while (i < len(self.correctResult)-1):

            doc.add_paragraph(self.correctResult[i])

            i += 1

        doc.save(savePath)
