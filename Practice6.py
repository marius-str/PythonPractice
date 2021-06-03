# >>> Handling Multiple Conditions <<<

province = input('What province do you live in? ')
tax = 0

# If multiple values cause the same output you can combine them by listing all
# values you want to check for with the in operator
if province in ('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

print(tax)
#############################################################
province = input("What province do you live in? ")
tax = 0
if province == 'Alberta' \
        or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)
#############################################################

# nested if statement
country = input("What country do you live in? ")

if country.lower() == 'canada':
    province = input('What province do you live in? ')
    if province in ('Alberta',
                    'Nunavut',
                    'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0

print(tax)
##################################################

# multiple "if" statements
province = input("What province do you live in? ")
tax = 0

if province == 'Alberta':
    tax = 0.05
if province == 'Nunavut':
    tax = 0.05
if province == 'Ontario':
    tax = 0.13

print(tax)
