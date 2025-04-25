#print('Hello World')

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2 if num2 != 0 else 'undefined'

print(f'Sum: {sum}')
print(f'Difference: {diff}')
print(f'Product: {prod}')
print(f'Quotient: {quot}')
print('End of program')
