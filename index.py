
class StudentDatabase:
    _student_list = []
    @classmethod
    def add_student(self, student):
        self._student_list.append(student)
    @classmethod
    def view_all_students(self):
        if not self._student_list:
            print("No students in the database.")
            return
        print("\n-- All Students --")
        for student in self._student_list:
            student.view_student_info()
    @classmethod
    def student_exists(self, student_id):
        for student in self._student_list:
            if student.student_id == student_id and student._is_enrolled == True:
                return True
        return False
    @classmethod
    def get_student_by_id(self, student_id):
        for student in self._student_list:
            if student.student_id == student_id:
                return student
        return None
class Student(StudentDatabase):
    def __init__(self, student_id, name, department, is_enrolled=False):
        self._student_id = student_id  
        self._name = name  
        self._department = department   
        self._is_enrolled = is_enrolled   
        StudentDatabase.add_student(self)
    @property
    def student_id(self):
        return self._student_id
    def enroll_student(self):
        if not self._is_enrolled:
            self._is_enrolled = True
            print(f"Student {self._name} is now enrolled.")
        else:
            print(f"Student {self._name} is already enrolled.")
         
                    

    def drop_student(self):
        if self._is_enrolled:
            self._is_enrolled = False
            print(f"Student {self._name} dropped.")
        else:
            print(f"Student {self._name} is already not enrolled.")

    def view_student_info(self):
        enrollment_status = "True" if self._is_enrolled else "False"
        print(f"Student ID: {self._student_id}, Name: {self._name}, Department: {self._department}, Enrollment Status: {enrollment_status}")
  
        

Student("S001", "Farhan", "Computer Science", is_enrolled=True)
Student("S002", "Rakib", "Mathematics", is_enrolled=False)
Student("S003", "Sakib", "Physics", is_enrolled=True)

flag = True
while flag:
    print('--- Student Management Menu ---')
    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')
    a = int(input('Enter your choice (1-4): '))
    if a == 1:
        StudentDatabase.view_all_students()
    elif a == 2:
        student_id = input("Enter Student ID to Enroll: ")
        student = StudentDatabase.get_student_by_id(student_id)
        if student:
            student.enroll_student()
        else:
            print("Student not found!")
    elif a == 3:
        student_id = input('Enter Student ID to Drop: ')
        student = StudentDatabase.get_student_by_id(student_id)
        if student:
            student.drop_student()
        else:
            print("Student not found!")
    elif a == 4:
        flag= False
    else:
        print("Invalid choice! Please insert a correct option.")