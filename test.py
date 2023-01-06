import csv
import os


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

lastLabel = '21.jpg'
i = len(lastLabel)-1
s = 0
j = 0
while (i >= 0):
    if lastLabel[i].isdigit():
        s += int(lastLabel[i])*(10**j)
        j += 1
    i -= 1
lastLabel = s
print(lastLabel)
