from datetime import datetime, timedelta

# Working with Dates
birthday = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday, '%d%m%Y')

print('Birthday: ' + str(birthday_date), '\n')

###############################################
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day

print('Day before birthday: ' + str(birthday_eve))
###########################################

# >>> Get Current Date <<<
current_date = datetime.now()

print('Today is: ' + str(current_date))
########################################
today = datetime.now()

print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second) + '\n')
########################################

# >>> Date Functions <<<

today_date = datetime.now()

print('Today is: ' + str(today_date))

one_day = timedelta(days=1)

yesterday_date = today_date - one_day

print('Yesterday was: ' + str(yesterday_date))

one_week = timedelta(weeks=1)
last_week = today - one_week

print('Last week was: ' + str(last_week))

