score = input('Enter Score ')
score = float(score)
#score must fall between 0.0 and 1.0
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
else:
    print('That is not a valid score')
    exit()
