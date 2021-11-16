import re
file = input('Enter a file: ') #Prompting user for input
try: #Checking to see if input is a valid file
    rawtext = open(file) #Opening file
except:
    print('That is not a valid file.')#Printing to screen
    exit() #Exiting after print to screen if file cant be opened

frql = dict()
for line in rawtext:
    srch = re.findall('([a-z])', line)
    for srchs in srch:
        frql[srchs] = frql.get(srchs, 0) + 1

sorted_dict = frql.keys()
sorted_dict = sorted(sorted_dict)
for key in sorted_dict:
    print(key,':', frql[key])
