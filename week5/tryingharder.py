count = 0 #Setting Value for count
total = 0 #Setting Value for total

while True:#Starting Loop
    usernum = input('Enter a number: ') #prompting user for a number
    if usernum == usernum:
        count = count + 1 #starting counter in loop
        try: #using try/except to make sure user entered a number and not a character or if there done
            usernum = float(usernum) #turning usernum into float
        except: #checking to see if the user is done
            if usernum == 'done': #user is done
                break #breaking from loop
            else: #if the input cant be converted to a float or does not equal done
                usernum = 0 #value becomes zero
                if usernum > -1: #0 always more than negative one
                    print('bad number') #printing bad number to screen
                    exit() #ending program
        total = (usernum + total) #keeping track of all vlaues and adding together
        
print(total, count, (total/count)) #printing the fruits of my labor

####This was definetly a challenge, and took me quite a few trys to get it right, thank you!####
