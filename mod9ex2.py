file = input('Enter a file: ')
try:
    rawtext = open(file)
except:
    print('That is not a valid file.')

wrdlst = dict()
for word in rawtext:
    if word.startswith('From '):
        words = word.split()
        month = words[2]
        if month not in wrdlst:
            wrdlst[month] = 1
        else:
            wrdlst[month] += 1

print(wrdlst)
