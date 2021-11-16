import urllib.request

fhand = urllib.request.urlopen(input('Enter - '))

word = list()
for line in fhand:
    line = line.decode().strip()
    print(line)
    if line not in word:
        for words in line:
            a = words.split()
            word.append(a)
        continue

print(len(word))
