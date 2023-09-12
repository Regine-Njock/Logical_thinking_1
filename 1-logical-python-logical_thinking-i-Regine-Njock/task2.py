import datetime


def isweekend(date):
    if date.weekday() == 5 or date.weekday() == 6:
        return True
    return False





print(isweekend(datetime.date(2021, 8, 6)))
print(isweekend(datetime.date(2021, 8, 7)))
print(isweekend(datetime.date(2021, 8, 8)))
print(isweekend(datetime.date(2021, 8, 9)))
            
    