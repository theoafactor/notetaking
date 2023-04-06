from includes import user_include

option = user_include.startApp()

if option == '5':
    print("Goodbye!")
    exit()

elif option == "4":
    print("Listing all users ...")
    from os import path
    result = path.exists("users.py")

    if result is True:
        ## file exists already
        import users
        users = users.users
        print("---------------------------------")
        print("Username    |    User Email")
        print("---------------------------------")
        for user in users:
            print(user['username'] + "     |     " +user['useremail'])
    else:
        ## the file does not exist
        print("There are no users at the moment")

elif option == '1':
    print("Creating new account ")
    user = user_include.getUserData()
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





