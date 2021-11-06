fn = input('Enter file name: ')#prompting for file name
try:#testing to see if file exists, if not exit
    fhand = open(fn)
except:
    if fn == 'I FINALLY GOT IT':
        print('Heres a cookie... i mean a easter egg... a cookie flavored easter egg')
        print('ʕ●¯ᴥ¯●ʔ>0')
        exit()
    else:
        print('That file does not exist')
        exit()

count = 0 #Starting value for count
total = 0 #Starting value for total
for line in fhand: #Counting number of lines that start with quoted string
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1 #Adding 1 to our count to determine number of applicable strings
        lines = line.find(':') #Searching for ':' in string
        numbers = line[lines+1: ] #Starting from the character right after position of ':'
        numbers = float(numbers) #Extracts numbers in string and floats it
        total = (total + numbers) #Adding numbers extracting to our total value

print('Average Spam Confidence:', count, total/count) #Printing to screen the average,
# average based on 'total' value divided by number of lines that started with given string
