fn = input('Enter a file name: ')#Prompting user for file name
try:#Checking to see if user inputed valid file
    fh = open(fn)#storing file handle in fh
except:
    print('Note a valid file.')
    exit()#exiting after print if file is not valid

count = 0#Giving count a zero value
for line in fh:#Parsing file
    if line.startswith('From '):#Looking for lines that star with From
        count = count + 1#Adding one to count for each instance
        newline = line.split()#Splitting line by spaces
        print(newline[1])#printing first word in lines that start with From

print('There were', count, 'lines in the file with From as the first word.')
#Printing count inside of string
