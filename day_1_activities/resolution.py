# -----------------------------------------
# Existing student data (example starter)
# -----------------------------------------
students = [
    {
        "CPSid": "123456",
        "name": "Lopez, Maria",
        "middlename": "Isabel",
        "homeroom": "301",
        "grade": 7,
        "primemail": "mlopez@cps.edu",
        "secoemail": "mlopez2@cps.edu"
    },
    {
        "CPSid": "789012",
        "name": "Johnson, Malik",
        "middlename": "Andre",
        "homeroom": "204",
        "grade": 8,
        "primaemail": "mjohnson@cps.edu",
        "secoemail": "mjohnson2@cps.edu"
    }
]


# -----------------------------------------
# SEARCH FUNCTION
# -----------------------------------------
def search_student(fullname):
    """
    Students must be able to describe this process:
    - Loop through the list of student dictionaries
    - Compare the 'name' field to the search term
    - If found, return the dictionary
    - If not found, return None
    """
    # first step: 
    # create a loop to loop throughthe students
    for student in students:
        if student["name"].lower() == fullname.lower():
            return student
        else:
            return None
    # then compare the name field to the search term
       
            # if found, return the dictionary
            
    # if not found, return None
    


# -----------------------------------------
# ADD NEW STUDENT FUNCTION
# -----------------------------------------
def add_student():
    print("\n--- Add a New Student ---")

    # Get user input for all required fields
    CPSid = input("CPS ID:   ")

    # Check for duplicate CPS ID
    # Loop through existing students to see if cps_id already exists
    for student in students:
        if student["CPSid"] == CPSid:
            print("A student with this ID already exists.")
            return
        else:
            first = input("First Name: ")
            last = input("Last Name: ")
            middle = input("Middle Name: ")
            homeroom = input("Homeroom: ")
            grade = int(input("Grade Level: "))
            primary = input("Primary Email: ")
            secondary = input("Secondary Email: ")
            fullname = f"{last}, {first}"
            new_student = {
                "cps_id": CPSid,
                "name": fullname,
                "middlename": middle,
                "homeroom": homeroom,
                "grade": grade,
                "primary_email": primary,
                "secondary_email": secondary
            }
            break

        # Add to the list
    students.append(new_student)    

    # Confirmation
    print("Student added successfuly.")
    print(new_student)
    print("---")
    print("List of current students")
    for student in students:
        print(student)
    print("---")


# -----------------------------------------
# MAIN PROGRAM LOOP
# this is where the program starts running

# -----------------------------------------
while True:
    # Menu
    print("\n===== STUDENT LOOKUP TOOL =====")
    print("1. Search for a student")
    print("2. Add a new student")
    print("3. Quit")

    # Get user choice
    choice = input("Choose an option: ")
    # Handle user choice
    if choice == "1":
        # Search for a student
        name = input("\nEnter the student's full name (Last, First):  ")
        result = search_student(name)
        # Call the search function and store the result
        
        

        # Display results
        if result:
           print("\nStudent found.")
           print(f"CPS ID: {result['CPSid']}")
           print(f"Name: {result['name']}")
           print(f"Middle Name: {result['middlename']}")
           print(f"Homeroom: {result['homeroom']}")
           print(f"Grade: {result['grade']}")
           print(f"Primary Email: {result['primemail']}")
           print(f"Secondary Email: {result['secoemail']}")
    
        else:
            # Inform the user if the student was not found
            print("\nStudent not found.")

    elif choice == "2":
        add_student()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")  