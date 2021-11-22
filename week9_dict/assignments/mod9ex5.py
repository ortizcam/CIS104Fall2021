file = input('Enter a file: ')#Prompting user to enter file name
try:#Making sure user input is a valid file
    rawtext = open(file)#Trying to open file name given
except:
    print('That is not a valid file.')
    exit()#Ending if file cant be opened

domains = dict()#Creating a dictionary called domains
emails = list()#Creating a list called emails
for word in rawtext:#Parsing the text in file
    if word.startswith('From '):#Checking for lines that start with from
        words = word.strip()#Stripping /n
        words = word.split()#Splitting into words
        email = words[1]#Putting position one value into email variable
        emails.append(email)#Adding email to emails list
for doma in emails:#Parsing emails list
    d = doma.split('@')#Splitting at the @ symbol
    domain = d[1]#Putting position one value into domain variable
    domains[domain] = domains.get(domain, 0) + 1#Checking to see if domain is in dictionary
    #if domain not in dictionary, assign default value, if it is add one to value
print(domains)#Print domains dictionary, showing the number of times the specific domain of an email appeard in file
