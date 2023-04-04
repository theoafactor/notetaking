## ask the user for their names 
username = input("Enter your name: ")

# ask the user for their email
useremail = input("Enter your email: ")

## user dictionary to represent the data
user = {
    "username": username,
    "useremail": useremail
}

## typecast the user dictionary to a string
#user = str(user)

## check if the users.py file exists
from os import path

result = path.exists("users.py")

if result == True:
    ## the file exists already
    print("The file exists already")
    import users
    users_list = users.users

    users_list.append(user)
    
    fileobject = open("users.py", "w")

    users_list = "users="+str(users_list)

    fileobject.write(users_list)

    print("user added successfully!")

    fileobject.close()



else:
    print("The file does not exist")
    print("Creating the file users.py ...")
    fileobject = open("users.py", "w")

    users_list = []
    users_list.append(user)
    users_list = str(users_list)
    data = "users=" + users_list

    fileobject.write(data)

    print("user added successfully!")

    fileobject.close()





