# Handling Conditions
country = input('Enter name of home country: ')

if country == 'canada':
    # string comparisons are case-sensitive
    # if you typed in CANADA or Canada it will not match
    print('You must like hockey!')
else:
    print('You are not from Canada')

#########################################################
price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
    # Anything that costs $1.00 or more is charged 7% tax
    # All statements indented are only executed if price is > = 1
    tax = .07
    print('Tax rate is ' + str(tax))
else:
    # Anything else we do not charge any tax
    # All statements indented are only executed if price is NOT >= 1
    tax = 0
    print('Tax rate is: ' + str(tax))
###################################################################
price = 5.0

if price >= 1.00:
    tax = .07
else:
    tax = 0

print(tax)
#########################
country = 'CANADA'

if country.lower() == 'canada':
    print('Hello eh')
else:
    print('Hello')
######################################
# Calculate the tax
# Anything purchased for more than $1.00 is charged a 7% tax
price = input('how much did you pay? ')

# Convert the string to a number
price = float(price)

# Check if the price is greater than 1.00
if price >= 1.00:
    # Everything over $1.00 is charged 7% tax
    tax = .07
    print('Tax rate is: ' + str(tax))
