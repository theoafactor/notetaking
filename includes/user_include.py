def startApp():
    print(" ----- Welcome to Note Taking App ---- ")
    print("Please choose Menu Option: ")
    print("""
1. Create Account
2. Log in
3. Create Note
4. List Users
5. Exit
    
    """)

    option = input("Please enter one option: ")
    
    return option



def getUserData():
    ## ask the user for their names 
    username = input("Enter your name: ")

    # ask the user for their email
    useremail = input("Enter your email: ")

    ## user dictionary to represent the data
    user = {
        "username": username,
        "useremail": useremail
    }

    return user