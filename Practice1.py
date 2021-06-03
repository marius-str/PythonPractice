print("Hello there", '\n')
print('Hello there')
####################
print('Hello World', '\n')
####################

name = input('Enter a name to display: ')
print(name)

# this is a comment

'''
this is a comment
on a
different
line
'''
#######################

name = "Jack"


def printname(myname):
    # this function receives a name parameter and prints it
    print("##########################")
    print("in printname() function")
    print(myname)
    print("##########################")


printname(name)

# >>> String Variables <<<

first_name = 'Susan'
print(first_name)

#######################
sentence = 'This is a dog'

print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print('i appears', sentence.count('i'), 'times in the sentence')
#######################
first = input('What is your first name? ')
middle = input('What is your middle name? ')
last = input('What is your last name? ')

# formatting strings in the print statements
# wrapping on different lines
print('Hello ' + first.capitalize() + ' '
               + middle.capitalize() + ' '
               + last.capitalize())

# combining strings
print('Hi ' + first + ' ' + last)
#######################
