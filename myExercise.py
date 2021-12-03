import sys
class StudentError(Exception):
    pass
with open(sys.argv[1], "r", encoding="utf-8") as file:
    lines = file.readlines()
    dictStudents = {i.strip("\n ").split(":")[0]: i.strip("\n ").split(":")[1] for i in lines if not i.strip("\n ") == "" }
    def datastudents(students):
        studentlist = students.split(",")
        for i in studentlist:
            try:
                if i not in dictStudents.keys():
                    raise StudentError
                print(f"Name: {i}, University: {dictStudents[i]} ",end="")
            except StudentError:
                print(f"No record of '{i}' was found! ",end = "")
datastudents(sys.argv[2])

