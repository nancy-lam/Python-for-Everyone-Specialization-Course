# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
cel = float(input('Celsius temperature = ').strip())
fah = (cel * 9/5) + 32
print(f'-> Fahrenheit temperature = {fah}')