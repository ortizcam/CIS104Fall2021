import re #Import regular expressiosn
inp = input('Enter a regular expression: ') #Having user input a expression
hand = open('mbox.txt') #Opening mbox file
count = 0 #Creating counter

for lines in hand: #Parsing file
    lines = lines.rstrip() #Stripping lines
    srch = re.findall(inp, lines) #Finding all lines that match inp
    if len(srch) > 0: #if len of srch larger than 0
        count = count + 1 # Add one to the counter

print('mbox.txt had', count, 'lines that matched', inp) #Printing number of istances in a nice string
