import csv
import os
import cv2 as cv
import easyocr
import numpy as np

num = 352.9991573
print(np.round(num).astype(int))

# labels = open(f'{os.getcwd()}/Dataset/labels.csv', 'r+', newline='')
# # code for, if file is empty or there's just column names no entries
# # labelLines = list(csv.reader(labels))
# labelLines = csv.reader(labels)

# print(labelLines)

# # lines = 0
# # print(labels.readlines()[-1][0])
# for lines in labelLines:
#     pass
# print(lines[0])
# labels.close()

# lastLabel = '21.jpg'
# i = len(lastLabel)-1
# s = 0
# j = 0
# while (i >= 0):
#     if lastLabel[i].isdigit():
#         s += int(lastLabel[i])*(10**j)
#         j += 1
#     i -= 1
# lastLabel = s
# print(lastLabel)

result = ['som3', 'text', 'f@r', 'te$t']

tempTxt = open('temp.txt', 'w', newline='')

# tempTxt.writelines(result)

i = 0
while (i < len(result)):
    tempTxt.write(f'{result[i]}_,_')
    i += 1

tempTxt.close()
# os.system('cmd /k "start temp.txt"')


tempTxt = open('temp.txt', 'r')
# i = 0
# while (i < len(result)):
#     print(tempTxt.readline())
#     i += 1
result = tempTxt.readline().split(sep='_,_')
print(result)
tempTxt.close()
