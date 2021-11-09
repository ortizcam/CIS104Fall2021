inp = input('Enter a file: ')#prompting user for a file
try: #making sure input was a file that could be opened
    file = open(inp) #opening inputted file and storing in file
    if True:
        poem = file.read() #reading file and storing in poem
        indv = poem.strip()#stripping poem and storing in indv
        words = indv.split()#splitting indiv and storing in words

except:#exiting if file did not exist
    print('Invalid file')
    exit()

ogwords = list()#Making a empty list called ogwords
for finalwords in words:#Traversing through the words list with finalwords
    if finalwords in ogwords:#Checking to see if the finalwords are in ogwords list
        continue #If the word is found skip it, if not next line
    ogwords.append(finalwords)#Append finalwords to ogwords list
    ogwords.sort() #sorting list in ascending order by default

print(ogwords)#Printing our final results
