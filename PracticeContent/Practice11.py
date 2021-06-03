from datetime import datetime


# >>> Functions <<<


def print_time(task_name: str):
    """
    Define a function to print the current time and task name

    :param task_name: str
    :return: N/A
    """

    print(task_name)
    print(datetime.now())
    print()


first_name = 'Susan'

# Call print_time() function to display message and current time
# pass in name of task completed
print_time('first name assigned')

for x in range(0, 10):
    print(x)

print()
print_time("loop completed")


########################################

# Getting clever with functions


def get_initial(name: str):
    """
    Get initial letter from name and capitalize it

    :param name: str
    :return: initial letter capitalized
    """
    initial = name[0:1].upper()

    return initial


# Ask for name
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")

# Call get_initial function to return first letter of a name
print('Your initials are: '
      + get_initial(first_name)
      + get_initial(middle_name)
      + get_initial(last_name))
