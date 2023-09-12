username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
#valid = {"username": "admin", "password": "admin"}
if username==password:
    print(f'Welcome, {username}')
else:
    print('Credentials are invalid')
