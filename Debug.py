from datetime import date, timedelta
from typing import List

def find_sundays_between(start: date, end: date) -> List[date]:
    total_days: int = (end - start).days + 1
    sunday: int = 6
    all_days = [start + timedelta(days=day) for day in range(total_days)]
    return [day for day in all_days if day.weekday() is sunday]


date_start: date = date(2001, 4, 18)
date_end: date = date(2099, 2, 12)
sundays = find_sundays_between(date_start, date_end)
count=0
for days in sundays:
    if(days.day==13):
        count+=1

print(count)