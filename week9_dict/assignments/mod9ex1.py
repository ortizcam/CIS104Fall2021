inp = input('Enter a file: ')
try:
    file = open(inp)
    if True:
        words = file.read()
        kwords = words.rstrip()
        jwords = kwords.split()
except:
    print('That is not a valid file.')
    exit()

wrdlst = dict()
for dwords in jwords:
    wrdlst[dwords] = 0

print(wrdlst)
