# Write your solution here
from datetime import datetime

millenium_time = datetime(1999, 12 ,31)

user_day = int(input('Day: '))
user_month = int(input('Month: '))
user_year = int(input('Year: '))

user_birth = datetime(user_year, user_month, user_day)

if user_birth > millenium_time:
    print('You weren\'t born yet on the eve of the new millennium.')
else:
    difference = millenium_time - user_birth
    print(f'You were {difference.days} days old on the eve of the new millennium.')


