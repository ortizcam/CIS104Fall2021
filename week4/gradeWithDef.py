score = input('Enter Score ') #Prompting user for there grade
try:
    score = float(score)
except:
    score = -1
    print('bad score')
    exit() #Making sure the users input is not a character

score = float(score) #Converting score into a float
#score must fall between 0.0 and 1.0
def computegrade(score):
    if score == str(score):
        return 'bad score'
    elif score >= 1:
        return 'Bad Score'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    elif score <= 0.6:
        return 'F'
    else:
        print #Defining computegrade function, assigning character grades to values

print (computegrade(score))#Outputting grade to users screen
