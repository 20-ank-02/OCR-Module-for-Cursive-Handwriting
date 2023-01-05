stg = '1146.jpg'
s = 0

i = len(stg)-5
print(i)
while (i >= 0):
    s += int(stg[i])*(10**((len(stg)-5)-i))
    i -= 1


print(s)
