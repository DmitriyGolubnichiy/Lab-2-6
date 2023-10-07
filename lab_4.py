
import datetime

from datetime import timedelta

current_date = datetime.datetime.now()

curr_year = current_date.year

curr_month = current_date.month

dayOfMonth = datetime.datetime(curr_year , curr_month , 1)

while dayOfMonth.weekday() != 2:
    dayOfMonth += timedelta(days=1)

thirdWed = dayOfMonth + timedelta(weeks=2)

print(thirdWed)

