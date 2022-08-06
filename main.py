# =========================
# simple program to practice sort
# data is list of lists
# output data based on user request / choice
# =========================

students = [("Andy", 'C', 20, "Pysic"),
            ("Pesky", 'A', 24, "Statistic"),
            ("Windy", 'D', 26, "Art"),
            ("Mandy", 'B', 22, "Math")]

name = lambda stud_name: stud_name[0]
grade = lambda stud_grade: stud_grade[1]
age = lambda  stud_age: stud_age[2]
major = lambda stud_major: stud_major[3]

print("\n== Students Data ==")
print("1. Display data")
print("2. Display - Sort by name")
print("3. Display - Sort by grade")
print("4. Display - Sort by age")
print("5. Display - Sort by major")
print("e. Exit")
choice = input("choice: ").lower()      # user input to lower case - simpler while-loop condition

while choice != 'e':
    if choice == '1':
        print("\n = Display data =")
        for i in students:              # display normally
            print(i)

    elif choice == '2':
        print("\n = Display - Sort by Name =")
        students.sort(key=name)
        for i in students:             # display with name has been sorted
            print(i)

    elif choice == '3':
        print("\n = Display - Sort by Grade =")
        students.sort(key=grade)
        for i in students:
            print(i)

    elif choice == '4':
        print("\n = Display - Sort by Age =")
        students.sort(key=age)
        for i in students:
            print(i)

    elif choice == '5':
        print("\n = Display = Sort by Major =")
        students.sort(key=major)
        for i in students:
            print(i)

    else:
        print("\n[ Invalid choice ]")

    print("\n== Students Data ==")
    print("1. Display data")
    print("2. Display - Sort by name")
    print("3. Display - Sort by grade")
    print("4. Display - Sort by age")
    print("5. Display - Sort by major")
    print("e. Exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
