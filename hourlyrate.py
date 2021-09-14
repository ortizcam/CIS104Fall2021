# Asking the user for how many hours they worked then what there rate of pay is.
hours = input('How many hours did you work? ')
rate = input('What is your hourly rate? ')
# Turning both inputs into floats, so if user inputs a decimal it is still usable.
hours = float(hours)
rate = float(rate)
# Calculating pay rate.
pay = hours * rate
# Telling the user what there total pay will be based on there inputs.
print('Your total pay will be', pay)
