file = input('Enter a file: ')#Prompting user for input
try:#Checking to see if input is a valid file
    rawtext = open(file)#Opening file
except:
    print('That is not a valid file.')
    exit() #Exiting after print to screen if file cant be opened

wrdlst = dict()#Creating empty dictionary
for word in rawtext:#Parsing rawtext
    if word.startswith('From '):#Checking to see if line starts with from
        words = word.split()#Splitting by spaces to seperate words in line
        email = words[1]#Setting the value of email to position one text
        if email not in wrdlst:#Checking to see if email is not in dictionary
            wrdlst[email] = 1#If not change value to 1
        else:
            wrdlst[email] += 1#If it is add one to value

largestnum = None#Setting None value to variable
largestword = None#Setting none value to variable
for word,count in wrdlst.items():#Parsing key value pairs in wrdlst
    if largestnum is None or count > largestnum: #Checking to see if value is larger than what is in the variable largest num
        largestword = word#if value is larger, assign key to largestword
        largestnum = count#if value is larger, assign value to largestnum


print(largestword, largestnum)#Printing to screen largest key value pair out of the wrdlst dict
