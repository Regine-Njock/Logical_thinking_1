users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]
def get_user(arg1,arg2):
    for user in users:
        if arg1 == user['name'] and arg2 == user['password']:
            print(user)
            return user
    print('An err occurred, you are not authorized')

username = i
    
    