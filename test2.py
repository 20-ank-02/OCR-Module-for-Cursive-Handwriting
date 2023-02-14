import os
import csv

listdir = (os.listdir(f'{os.getcwd()}/Dataset'))

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
            s += int(lastLabel[i])(10*j)
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

for i in range(41):
    # labeling
    if os.path.exists(f'{os.getcwd()}/Dataset/{listdir[i]}'):
        continue
    else:
        if listdir[i] != 'labels.csv':
            os.rename(
                f'{os.getcwd()}/Dataset/{listdir[i]}', f'{os.getcwd()}/Dataset/{i+1}.jpg')
    writerObj.writerow(
        {'filename': f'{lastLabel+i+1}.jpg', 'words': 'a'})

labels.close()
