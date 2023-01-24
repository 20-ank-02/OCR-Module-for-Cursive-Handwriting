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


class OCR():
    def __init__(self):
        super.__init__()

    def variables(self, d):
        self.detailCheck = d

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

    def imgRead(self):
        # this needs to run only once to load the model into memory
        self.imG = cv2.imread('test case.jpg')
        reader = easyocr.Reader(['en'], gpu=True)
        self.result = reader.readtext(self.imG, detail=1)

    def rect(self):
        for i in range(len(self.result)-3):
            topLeft = self.result[i][0][0]  # [146, 134]
            bottomRight = self.result[i][0][2]  # [537, 268]
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
    # rect = cv2.rectangle(imG, topLeft, bottomRight, (255, 255, 0), thickness=3)
        cv2.imshow('result', rect)

    def Label(self):

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
        for i in range(len(self.result)-3):
            # labeling
            self.writerObj.writerow(
                {'filename': f'{self.lastLabel+i+1}.jpg', 'words': self.result[i][1]})

            # cropping image
            self.topLeft = self.result[i][0][0]
            self.bottomRight = self.result[i][0][2]

            croppedImg = self.imG[self.topLeft[1]: self.bottomRight[1],
                                  self.topLeft[0]: self.bottomRight[0]]

            # saving cropped image
            cv2.imwrite(f'{os.getcwd()}/Dataset/{self.lastLabel+i+1}.jpg',
                        croppedImg)  # f-strings

        self.labels.close()

    def docx(self):
        # result = ['som3', 'text', 'f@r', 'te$t']

        # tempTxt = open('temp.txt', 'w', newline='')

        # # tempTxt.writelines(result)

        # i = 0
        # while (i < len(result)):
        #     tempTxt.write(f'{result[i]}_,_')
        #     i += 1

        # tempTxt.close()
        # # os.system('cmd /k "start temp.txt"')

        # tempTxt = open('temp.txt', 'r')
        # # i = 0
        # # while (i < len(result)):
        # #     print(tempTxt.readline())
        # #     i += 1
        # result = tempTxt.readline().split(sep='_,_')
        # print(result)
        # tempTxt.close()

        # Creating document template
        doc = docx.Document()

        doc.add_paragraph(self.result[i][1])

        doc.save('result_text.docx')

        # closing all opened windows and files
        cv2.destroyAllWindows()

        # cmd command to open ms word of result.docx
        opt = input('Show document?(y or n)= ')

        if opt == 'y':
            os.system('cmd /c "start result_text.docx"')
        else:
            SystemExit()


# # caputering pressed key
# k = cv2.waitKey(0)

# if k == 27:
