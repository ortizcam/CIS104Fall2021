file = input('Enter a file: ')
try:
    rawtext = open(file)
except:
    print('That is not a valid file.')
    exit()

wrdlst = dict()
for word in rawtext:
    if word.startswith('From '):
        words = word.split()
        email = words[1]
        if email not in wrdlst:
            wrdlst[email] = 1
        else:
            wrdlst[email] += 1

print(wrdlst)
