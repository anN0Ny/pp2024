# Base parent class for Student and Course to inherit
class Entity:
    def __init__(self, entity_id, entity_name):
        self._id = entity_id
        self._name = entity_name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def display(self):
        print(f"ID: {self.get_id()}, Name: {self.get_name()}")

# Moved input_details function to System class for management (and braindead)
class Student(Entity):
    def __init__(self, student_id, student_name, birthdate):
        super().__init__(student_id, student_name)
        self._birthdate = birthdate

    def get_birthdate(self):
        return self._birthdate

    def display(self):
        print(f"Student ID: {self.get_id()} | Name: {self.get_name()} | Birthdate: {self.get_birthdate()}")

class Course(Entity):
    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)

    def display(self):
        print(f"Course ID: {self.get_id()} | Name: {self.get_name()}")

# Mark class inherit both classes above
class Mark(Student, Course):
    def __init__(self, student, course, score):
        Student.__init__(self, student.get_id(), student.get_name(), student.get_birthdate())
        Course.__init__(self, course.get_id(), course.get_name())
        self._score = score

    def get_score(self):
        return self._score

    def display(self):
        print(f"Student: {self.get_name()} (ID: {self.get_id()}), Course: {self.get_name()} (ID: {self.get_id()}), Score: {self.get_score()}")

class System:
    def __init__(self):
        # Separated entities into students and courses as it should be
        self.students = []
        self.courses = []
        self.marks = []

    def input_number(self, prompt):
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number
                print("Number must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def input_student(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        birthdate = input("Enter birthdate (DD/MM/YYYY): ")
        self.students.append(Student(student_id, student_name, birthdate))

    def input_course(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        if not self.courses or not self.students:
            print("Please add students and courses first.")
            return

        course_id = input("Select course by ID to input marks: ")
        course = self.find_by_id(course_id, self.courses)

        if not course:
            print("Course not found.")
            return

        for student in self.students:
            while True:
                try:
                    score = float(input(f"Enter score for {student.get_name()} (ID: {student.get_id()}): "))
                    if 0 <= score <= 20:
                        self.marks.append(Mark(student, course, score))
                        break
                    print("Score must be between 0 and 20.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def find_by_id(self, entity_id, entities):
        return next((entity for entity in entities if entity.get_id() == entity_id), None)

    def display_entities(self, entities, entity_type):
        if not entities:
            print(f"No {entity_type} available.")
            return
        for entity in entities:
            entity.display()

    def display_marks(self):
        course_id = input("Enter course ID to view marks: ")
        course = self.find_by_id(course_id, self.courses)

        if not course:
            print("Invalid Course ID.")
            return

        marks_for_course = [mark for mark in self.marks if mark.get_id() == course_id]
        if not marks_for_course:
            print("No marks available for this course.")
            return

        print(f"\nMarks for Course: {course.get_name()} (ID: {course.get_id()}):")
        for mark in marks_for_course:
            mark.display()

    def confirm_exit(self):
        while True:
            confirm = input("Do you wish to stay? ")
            if confirm.lower() == "yes" or confirm.lower() == "y":
                print("Please continue.")
                self.run()
            print("Thank you for using.")
            print("Now exiting...")
            break

    def run(self):
        #Added for exception handling(?) and technicality in function requirements
        num_students = 0
        num_courses = 0
        while True:
            print("\n===== Student Mark Management System =====")
            print("1. Input number of students in a class")
            print("2. Input student information: id, name, DoB")
            print("3. Input number of courses")
            print("4. Input course information: id, name")
            print("5. Select a course, input marks for student in this course")
            print("6. List students")
            print("7. List courses")
            print("8. Show student marks for a given course")
            print("Press any other keys to exit")

            choice = input("Choose an option: ")

            if choice == "1":
                num_students = self.input_number("Enter the number of students to add: ")
            elif choice == "2":
                for _ in range(num_students):
                    self.input_student()
            elif choice == "3":
                num_courses = self.input_number("Enter the number of courses to add: ")
            elif choice == "4":
                for _ in range(num_courses):
                    self.input_course()
            elif choice == "5":
                self.input_marks()
            elif choice == "6":
                self.display_entities(self.students, "students")
            elif choice == "7":
                self.display_entities(self.courses, "courses")
            elif choice == "8":
                self.display_marks()
            else:
                self.confirm_exit()
                break


if __name__ == "__main__":
    system = System()
    system.run()