print ("Welcome")

first_name = input("Please Enter Your First Name ")

last_name = input("Please Enter Your Last Name ")

def get_student_id():
    while True:
        student_id = input("Please enter your student ID: ")
        if is_valid(student_id):
            return student_id
        else:
            print("Invalid student ID. Please try again.")

def is_valid(student_id):
    # Example validation: student_id should be numeric and 8 digits long
    return student_id.isdigit() and len(student_id) == 8

student_id = get_student_id()
print(f"Welcome, student {student_id}!")
