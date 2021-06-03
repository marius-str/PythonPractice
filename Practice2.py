# >>> Numeric Variables <<<
pi = 3.14159
print(pi)

# Numbers treated as strings
first_num = input('Enter first number: ')
second_num = input('Enter second num: ')

# this concatenates numbers, just like strings
print(first_num + second_num)

# >>> Performing calculations <<<
n1 = 6
n2 = 2

print('addition')
print(n1 + n2)
print('subtraction')
print(n1 - n2)
print('multiplication')
print(n1 * n2)
print('division')
print(n1 / n2)
print('division with integral result')
print(n1 // n2)
print('exponent')
print(n1 ** n2)
print('modulus')
print(n1 % n2)

# Converting strings to numbers
print('###############################')

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
print('\n')

if num1.__contains__('.') or num2.__contains__('.'):
    print('Enter integers only! Exiting the program...')
else:
    # casting both variables to an int, to do calculations with them
    # by default, "input" variables are of type string
    print(int(num1) + int(num2))
    # casting both variables to a float, to do calculations with them
    print(float(num1) + float(num2))

print('###############################')

# Combining string and numbers

days = 28
days_in_feb = 'days in Feb'

print(days, ' days in Feb')

print(days, days_in_feb)
