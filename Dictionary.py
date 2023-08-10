# write a program to create student dictionary with n items
# each item is having name and course
n=int(input("Enter no of students"))
stud_dict={}
for i in range(n):
    name=input("Name of the students")
    course=input("Enter the name of the course")
    stud_dict[name]=course
print(stud_dict)
