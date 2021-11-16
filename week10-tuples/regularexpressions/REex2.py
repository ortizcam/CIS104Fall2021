import re #import regular expressions
inp = input('Enter a file: ')#Having user input a file handle
try:
    hand = open(inp)#Making sure file can be opened
except:
    print('That is not a valid file')#If file cant be opened print to screen
    exit()#Exit

count = 0 #Starting counter
num = list() #Creating empty list

for lines in hand: #Parsing file
    lines = lines.rstrip() #Stripping lines
    srch = re.findall('^New Revision: ([0-9]+)', lines) #Searching for lines that begin with " " pulling data that starts with a number from 0-9 following any matching characters after
    if len(srch) != 1 : continue #if length more than 1 continue
    nums = float(srch[0]) #Flaoting srch and storing in nums
    num.append(nums) #Appending nums to num
    count = count + 1 #Adding to count

print(int(sum(num)/count)) #Turning average of list into a int and print to screen
