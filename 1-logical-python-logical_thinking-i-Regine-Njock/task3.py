import datetime

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
#valid = {"username": "admin", "password": "admin"}
def isweekend(date):
    if username==password or date.weekday() >= 5:
        print(f'Welcome, {username}')
    elif username!=password or date.weekday() <= 5:

        print('Credentials are invalid')
        
print(isweekend(datetime.date(2021, 8, 7)))
print(isweekend(datetime.date(2021, 8, 6)))
