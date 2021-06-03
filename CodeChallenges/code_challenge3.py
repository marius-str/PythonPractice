from datetime import datetime, timedelta
# print today's date
today = datetime.now()

print('Today is: ' + str(today) + '\n')

# print yesterday's date
one_day = (timedelta(days=1))

yesterday = today - one_day

print('Yesterday was: ' + str(yesterday))
print('###################################################')

# ask a user to enter a date
date_entered = input('Please enter a date(dd/mm/yyyy): ')
date_entered = datetime.strptime(date_entered, '%d%m%Y')

# print the date one week from the date entered
one_week = timedelta(weeks=1)

next_week_date = date_entered + one_week

print('One week later it will be: ' + str(next_week_date))
