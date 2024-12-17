#. Write Python code to list name and roll number of 5 students in B.Sc. (Computer science).
students = []
choice = 1
while choice:
    rollno = int(input("Enter the roll no:-"))
    name = input("enter the name :-")
    students.append({"rollno" : rollno,"name":name})
    choice = int(input("Do you want to continue(0,1)?"))
print(students)
for student in students:
    print(f"student roll no:-{student['rollno']}\nstudent name:-{student['name']}")




# Enter the roll no:-1
# enter the name :-om
# Do you want to continue(0,1)?1
# Enter the roll no:-2
# enter the name :-s2
# Do you want to continue(0,1)?1
# Enter the roll no:-3
# enter the name :-s3
# Do you want to continue(0,1)?1
# Enter the roll no:-4
# enter the name :-s4
# Do you want to continue(0,1)?1
# Enter the roll no:-5
# enter the name :-s5
# Do you want to continue(0,1)?0
# [{'rollno': 1, 'name': 'om'}, {'rollno': 2, 'name': 's2'}, {'rollno': 3, 'name': 's3'}, {'rollno': 4, 'name': 's4'}, {'rollno': 5, 'name': 's5'}]
# student roll no:-1
# student name:-om
# student roll no:-2
# student name:-s2
# student roll no:-3
# student name:-s3
# student roll no:-4
# student name:-s4
# student roll no:-5
# student name:-s5
    