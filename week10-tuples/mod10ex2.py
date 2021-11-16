file = input('Enter a file: ') #Prompting user for input
try: #Checking to see if input is a valid file
    rawtext = open(file) #Opening file
except:
    print('That is not a valid file.')#Printing to screen
    exit() #Exiting after print to screen if file cant be opened

hrln = dict() #Creating empty dictionary

for lines in rawtext: #Parsing rawtext
    if lines.startswith('From '): #Checking to see if line starts with from
        dline = lines.find(':') #Searching for semi-colon
        time = lines[dline-2:] #Starting two positions back from first semi colon
        stime = time[0:2 ]#Creating variable and storing value between position 0 and 2
        hrln[stime] = hrln.get(stime, 0) + 1 #Creating a histogram for number of time value occuers

hoco = list() #Creating a empty list
for h, c in hrln.items(): #Parsing key value pairs in dictionary
    hours = h #Assigning key to hours
    count = c #Assigning value to count
    hoco.append((hours, count)) #Adding to empty list

hoco.sort(reverse = False) #Sorting list

for hour, count in hoco:
    print(hour, count) #Printing out hour and count once per iteration while parsing hoco
