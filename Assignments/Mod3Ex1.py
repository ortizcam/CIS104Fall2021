# Asking the user for how many hours they worked then what there rate of pay is.
hours = input('How many hours did you work? ')
rate = input('What is your hourly rate? ')
# Turning both inputs into floats, so if user inputs a decimal it is still usable.
hours = float(hours)
rate = float(rate)
pay = hours * rate
#listing variables and trying to figure out overtimee
if hours <= float(40):
    print('Your total pay will be', pay)
#still trying
else:
    hours > 40 
    overtime = hours - float(40)
    overtime = float(overtime)
#5 would be the overtime at 45 hours
    overtimerate = 1.5 * rate
    overtimerate = float(overtimerate)
#overtimerate would be 15
    overtimetotal = overtime * overtimerate
    overtimetotal = float(overtimetotal)
    normalpay = 40 * rate
    normalpay = float(normalpay)
    pay = overtimetotal + normalpay
# Calculating pay rate.
# Telling the user what there total pay will be based on there inputs.
    print('Your total pay will be', pay)
