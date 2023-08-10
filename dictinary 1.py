# write a program to create student_dict with n students
# each student is having name as key and subject marks as values
n=int(input("Enter no of students"))
student_dictionary={}
for i in range(n):
    name=input("Enter name of the students")
    marks=list(map(int,input("Enter no of marks").split()))
    student_dictionary[name]=marks
    if name not in student_dictionary:
               student_dictionary[name]=marks
    print(name,"name is exist")
print(student_dictionary)
               
