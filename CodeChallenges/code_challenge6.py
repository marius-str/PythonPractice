# Ask a user their name
first_name = input('Please enter your first name: ')

# If their first name starts with A or B
# tell them they go to room AB
if first_name.startswith('A') or first_name.startswith('B'):
    print('Go to room AB')
# IF their first name starts with C
# tell them to go to room CD
elif first_name.startswith('C'):
    print('Go to room CD')
else:
    # If their first name starts with another letter, ask for their last name
    # IF their last name starts with Z, tell them to go to room Z
    # if their last name starts with any other letter, tell them to go to room OTHER
    last_name = input('Please enter your last name: ')
    if last_name.startswith('Z'):
        print('Go to room Z')
    else:
        print('Go to room OTHER')

# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
