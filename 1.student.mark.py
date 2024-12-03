def numberOfStudents(command = "\nInput the number of students: "):
    return int(input(command))

def studentInput(numStudents):
    while numStudents <= 0:
        numStudents = numberOfStudents(command = "\nInvalid number of students, please try again: ")
    studentList = []
    for i in range(numStudents):
        print(f"Please enter the data of student #{i+1} below.\n")
        studentID = input("Enter student ID: ")
        name = input("Enter student name: ")
        birthdate = input("Enter student Date of Birth (DD/MM/YYYY): ")
        studentList.append({
            "ID": studentID,
            "Name": name,
            "Birthdate": birthdate,
            })
    return studentList

def numberOfCourses(command = "\nInput the amount of courses: "):
    return int(input(command))

def courseInput(numCourses):
    while numCourses <= 0:
        numCourses = numberOfCourses(command = "\nError, number of courses invalid. Try again: ")
    courseList = []
    for j in range(numCourses):
        print(f"Please enter the data for course number {j+1} below.\n")
        courseID = input("Enter course ID: ")
        name = input("Enter course name: ")
        courseList.append({
            "courseID": courseID,
            "name": name
        })
    return courseList

def markInput(courses, students):
    courseChoice = input("\nSelect your course by ID to input marks: ")
    while courseChoice not in [val for dic in courses for val in dic.values()]:
        courseChoice = input("\nError. Please pick another course by its ID: ")
    scoreSheets = []
    for studentID in students:
        studentMark = float(input(f"\nInput the score of student with ID of {studentID['ID']} for the course with ID of {courseChoice}: "))
        while studentMark < 0 or studentMark > 20:
            studentMark = float(input("\nInvalid score, please try again: "))
        scoreSheets.append({
            "studentID": studentID['ID'], 
            "score": studentMark
            })

    return {
        "courseID": courseChoice,
        "marks": scoreSheets
    }

def listingStudents(students):
    print("\nList of students:")
    if len(students) == 0:
        print("How come there are no students? Please input some in :(")
    for i in range(len(students)):
        print(f"\nStudent #{i+1}")
        for key, value in students[i].items():
            print(f"{key}: {value}")

def listingCourses(courses):
    print("\nList of Courses:")
    if len(courses) == 0:
        print("This is empty. Please add some courses in :(")
    for i in range(len(courses)):
        print(f"\nCourses #{i+1}")
        for key, value in courses[i].items():
            print(f"{key}: {value}")

def listingMarks(courseMarks, courseOfChoice):
    print(f"\nList of marks for course ID {courseOfChoice}:")
    found = False
    for course in courseMarks:
        if course["courseID"] == courseOfChoice:
            found = True
            for mark in course["marks"]:
                print(f"Student ID: {mark['studentID']} - Mark: {mark['score']}")
            break
    if not found:
        print("No marks available for the selected course.")

def main():
    studentAmount = 0
    studentList = []
    courseAmount = 0
    courseList = []
    courseMarks = []

    while True:
        print("\nStudent Mark Management version 75737468.0")
        print("\nList of functions:")
        print("1. Input number of students in a class")
        print("2. Input student information: id, name, DoB")
        print("3. Input number of courses")
        print("4. Input course information: id, name")
        print("5. Select a course, input marks for student in this course")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a given course")
        print("\nPress any other keys to exit.")

        choice = input("\nPress any key to continue: ")
        if choice == "1":
            studentAmount = numberOfStudents()
        elif choice == "2":
            studentList = studentInput(studentAmount)
        elif choice == "3":
            courseAmount = numberOfCourses()
        elif choice == "4":
            courseList = courseInput(courseAmount)
        elif choice == "5":
            courseMarks.append(markInput(courseList, studentList))
        elif choice == "6":
            listingCourses(courseList)
        elif choice == "7":
            listingStudents(studentList)
        elif choice == "8":
            choice = input("Please select your course by inputting its ID: ")
            listingMarks(courseMarks, choice)
        else:
            print("Thanks for using, have a nice day.")
            break

if __name__ == "__main__":
    main()