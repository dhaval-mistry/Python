cTemp = float(input('Enter temperature in Celsius: '))
fTemp = float(input('Enter temperature in Fahrenheit: '))

# Convert Celsius to Fahrenheit
ffTemp = (cTemp * 9/5) + 32
print(f'Temperature in Fahrenheit: {ffTemp}')

ccTemp = (fTemp - 32) * 5/9
print(f'Temperature in Celsius: {ccTemp}')


