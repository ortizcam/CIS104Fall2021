file = input('Enter a file: ')#Prompting user for input
try:#Checking to see if input is a valid file
    rawtext = open(file)#Opening file
except:
    print('That is not a valid file.')#Printing to screen 
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

tuplist = list()#Creating a empty list
for w, c in wrdlst.items():#Parsing wrdlst by key and value
    tuplist.append((w, c))#Appending tuples to tuplsit

tuplist.sort(reverse=True)#Reversing the order of key,value pairs

mostpopn = None#Setting None value to variable (most popular name)
mostpopc = None#Setting None value to variable (most popular count)
for w, c in tuplist:#Parsing key value pairs in tuplist
    if mostpopc is None or c > mostpopc: #Checking to see if value is larger than what is in the variable mostpopc
        mostpopn = w #if value is larger, assign key to mostpopn
        mostpopc = c #if value is larger, assign value to mostpopc
print(mostpopn, mostpopc)#Printing the email that appeared the most, and how many times it appeared
