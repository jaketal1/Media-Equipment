print ("Welcome")

first_name = input("Please Enter Your First Name ")

last_name = input("Please Enter Your Last Name ")


def checkid():
    flag = False
    max = 3
    minlength = 8
    attempts = 0

    while attempts < max:
        login = input("Please enter your student ID")
        if len(login) >= minlength: 
             flag = True
             return (login)
        break
    else:

     attempts = attempts + 1
     print("Student ID too short")
     print("You have",{attempts}, "Remaining")

     if attempts >= 3:
        print("you have exceeded the maximum number of attempts")
        print("All attempts used access denied")


login = checkid()
print(f"Welcome, student {login}!")
