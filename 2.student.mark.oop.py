# TODO TODO: Refactor and reorganise the code and its logic

# Base parent class for Student and Course to inherit
class Entity:
    def __init__(self, entity_id, entity_name):
        self.__id = entity_id
        self.__name = entity_name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}")


class Student(Entity):
    def __init__(self, student_id, student_name, birthdate):
        super().__init__(student_id, student_name)
        self.__birthdate = birthdate

    def get_birthdate(self):
        return self.__birthdate

    def display(self):
        print(f"Student ID: {self.get_id()} | Name: {self.get_name()} | Birthdate: {self.get_birthdate()}")

    def input_details(self):
        print("\nEnter Student Details")
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        birthdate = input("Enter student Date of Birth (DD/MM/YYYY): ")
        return Student(student_id, student_name, birthdate)


class Course(Entity):
    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)

    def display(self):
        print(f"Course ID: {self.get_id()} | Name: {self.get_name()}")

    def input_details(self):
        print("\nEnter Course Details")
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)

# Mark class inherit both classes above for more in-depth data output (?)
class Mark(Student, Course):
    def __init__(self, student: Student, course: Course, score):
        Student.__init__(self, student.get_id(), student.get_name(), student.get_birthdate())
        Course.__init__(self, course.get_id(), course.get_name())
        self.__score = score

    def get_score(self):
        return self.__score

    def display(self):
        print(f"Student: {self.get_name()} (ID: {self.get_id()}), Course: {self.get_name()} (ID: {self.get_id()}), Score: {self.__score}")

class StudentMarkManagementSystem:
    def __init__(self):
        self.entities = []  # Holds both students and courses
        self.marks = []

    def input_entity(self, entity_type):
        print(f"\nInput {entity_type} information")
        num_entities = self.input_number(f"Enter the number of {entity_type}s: ")

        for _ in range(num_entities):
            if entity_type.lower() == 'student':
                entity = Student("", "", "").input_details()
            elif entity_type.lower() == 'course':
                entity = Course("", "").input_details()
            else:
                print("Invalid entity type")
                return
            self.entities.append(entity)

    def input_marks(self):
        course_id = input("\nSelect course by ID to input marks: ")
        course = self.find_entity_by_id(course_id, Course)
        if not course:
            print("Course not found.")
            return

        for student in self.entities:
            if isinstance(student, Student):
                while True:
                    try:
                        score = float(input(f"Enter the score for {student.get_name()} (ID: {student.get_id()}): "))
                        if 0 <= score <= 20:
                            self.marks.append(Mark(student, course, score))
                            break
                        else:
                            print("Score must be between 0 and 20.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

    def find_entity_by_id(self, entity_id, entity_type):
        for entity in self.entities:
            if isinstance(entity, entity_type) and entity.get_id() == entity_id:
                return entity
        return None

    def display_entities(self, entity_type):
        print(f"\nList of {entity_type}s:")
        filtered_entities = [e for e in self.entities if isinstance(e, entity_type)]
        if not filtered_entities:
            print(f"No {entity_type}s available.")
        else:
            for entity in filtered_entities:
                entity.display()
        # TODO: Fix errors
        # List of <class '__main__.Course'>s:
        # No <class '__main__.Course'>s available.
        # List of <class '__main__.Student'>s:

    def display_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        course = self.find_entity_by_id(course_id, Course)
        if not course:
            print("Invalid Course ID.")
            return

        marks_for_course = [mark for mark in self.marks if mark.get_id() == course_id]
        if not marks_for_course:
            print("No marks available for this course.")
        else:
            print(f"\nMarks for Course: {course.get_name()} (ID: {course.get_id()}):")
            for mark in marks_for_course:
                mark.display()

    def input_number(self, prompt):
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number
                else:
                    print("Number must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def run(self):
        while True:
            print("\n===== Student Mark Management System =====")
            print("1. Input student information")
            print("2. Input course information")
            print("3. Input marks for a course")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks for a course")
            print("7. Exit")
            choice = input("\nChoose an option: ")

            if choice == "1":
                self.input_entity("student")
            elif choice == "2":
                self.input_entity("course")
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.display_entities(Student)
            elif choice == "5":
                self.display_entities(Course)
            elif choice == "6":
                self.display_marks()
            elif choice == "7":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    system.run()