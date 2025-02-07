#create class

class student:
    #attributes
    idno =""
    name =""
    course =""
    age =0
#creating objects
student1 =student()
student2 =student()

#userinput

student1.idno = input("Enter The Admin NO. ")
student1.name = input("Enter your name ")
student1.course = input("Course ")
student1.age = int(input("Enter Age : "))

#printing out the info
print("====================")

print("Admin No : ", student1.idno)
print("Name : ", student1.name)
print("Course : ", student1.course)
print("Age : ", student1.age)