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

student1.idno="BSE-01-0076/2025"
student1.name ="Egan"
student1.course ="BSE"
student1.age ="20"

student2.idno ="BBIT-07-0089/2025"
student2.name ="Alvin"
student2.course ="BBIT"
student2.age = 92

#print out the details

print(student1.idno)
print(student1.name)
print(student1.course)
print(student1.age)

print("Student 2")

print(student2.idno)
print(student2.name)
print(student2.course)
print(student2.age)