# Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = float(input('Enter Hours: ').strip())
rate = float(input('Enter Rate: ').strip())
if hours > 40:
    pay = 40 * rate + (hours-40) * 1.5 * rate
else:
    pay = hours * rate 
print(f'Pay: {pay}')
