print("Welcome")

first_name = input("Please Enter Your First Name: ")
last_name = input("Please Enter Your Last Name: ")

def checkid():
    flag = False
    max_attempts = 3
    length = 8
    maxlength = 8
    attempts = 0

    while attempts < max_attempts:
        login = input("Please enter your student ID: ")
        if len(login) == length: 
            flag = True
            return login
        
        attempts += 1
        print("Student ID too short")
        print(f"You have {max_attempts - attempts} attempts remaining.")

        if attempts >= max_attempts:
            print("You have exceeded the maximum number of attempts")
            print("All attempts used. Access denied.")
            return None

login = checkid()
if login:
    print(f"Welcome student {login} !")