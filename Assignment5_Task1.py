name1=input("Enter the student's name: ")
mark1= int(input(" marks: "))
stu_mark1= name1+"'s"+ " marks: " +str(mark1)

name2=input("Enter the student's name: ")
mark2= int(input(" marks: "))
stu_mark2= name2+"'s"+ " marks: " +str(mark2)


dict={ name1: mark1, name2: mark2}
print(dict)

if("Ayaan" in dict):
    print( "Student found.")
else:
    print("Student not found.")