fh = open('text/mbox-short.txt') #opening file

for lx in fh: #creating a loop
    ly = lx.rstrip() #striping file of /n at the end of each line
    print(ly.upper()) #printing file in uppercase
