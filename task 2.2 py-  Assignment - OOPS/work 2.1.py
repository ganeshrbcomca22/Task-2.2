import datetime

class RegistrationSystem:
    def __init__(self, max_students, start_date, end_date):
        self.max_students = max_students
        self.start_date = start_date
        self.end_date = end_date
        self.students = []

    def register(self):
        if len(self.students) >= self.max_students:
            print("Registration failed. Maximum number of students reached.")
            return
        
        if not self._is_registration_open():
            print("Registration failed. Registration period has ended.")
            return
        
        roll_number = input("Enter student's roll number: ")
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        
        self.students.append({
            "roll_number": roll_number,
            "name": name,
            "age": age
        })
        print("Registration successful.")

    def show_registered_students(self):
        if not self.students:
            print("No students registered yet.")
            return
        
        print("Registered Students:")
        for student in self.students:
            print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Age: {student['age']}")
    
    def _is_registration_open(self):
        current_date = datetime.datetime.now().date()
        return self.start_date <= current_date <= self.end_date


# Constants
MAX_STUDENTS = 3
START_DATE = datetime.date(2024, 4, 1)
END_DATE = datetime.date(2024, 4, 30)

# Main program
registration_system = RegistrationSystem(MAX_STUDENTS, START_DATE, END_DATE)

while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Show Registered Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        registration_system.register()
    elif choice == "2":
        registration_system.show_registered_students()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
