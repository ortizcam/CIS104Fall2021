import re #import regular expressions
inp = input('Enter a file: ')#Having user input a file handle
try:
    hand = open(inp)#Making sure file can be opened
except:
    print('That is not a valid file')#If file cant be opened print to screen
    exit()#Exit

num = list() #Creating empty list

for lines in hand: #Parsing file
    lines = lines.strip() #Stripping lines
    line = lines.split()
    srch = re.findall('\n?(\d+)\s?', lines) #Searching for lines that begin with " " pulling data that starts with a number from 0-9 following any matching characters after
    if srch != None or srch >= 1 : #Appending values in list until there are no more values to add
        num.append(srch)
    else:
        continue

anum = [int(item) for sublist in num for item in sublist] #Converting all items in list to individual int values
print(sum(anum))#Printing sum to screen
