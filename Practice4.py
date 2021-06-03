# >>> Error Handling <<<

x = 42
y = 206

if x == y:
    print('Success')
##########################
x = 206
y = 42

if x < y:
    print(str(x) + 'is greater than' + str(y))
########################################
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

try:
    print(a / b)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Cannot divide a number by 0!')
# except:
#     print('Sorry, something went wrong!')
finally:
    print("This line is always executed regardless of success or failure.")
