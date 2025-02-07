#creating class
class student:
#attributes
idno=""
name =""
course =""
age =0

#Method
def fee(self):
print("\n======STUDENT FEE DETAILS=========\n")
amttpay =float(input("Enter Amount to Pay:"))
amtpaid=float(input("Enter Amount paid:"))
balance =amttpay-amtpaid
print("\n===================\n")
print("Balance : ", balance)

#Method 2

def grade(self):
print("\n======STUDENT GRADING DETAILS=========\n")
oop1 = int(input("Enter OOP 1 Marks:"))
oop2 = int(input("Enter OOP 2 Marks:"))
dbms = int(input("Enter DBMS Marks:"))
total = oop1+oop2+dbms
avg =total/3
print("AVG: ", avg)
if avg >=70:
print("GRADE :A")
elif avg >=60:
print("GRADE: B")

elif avg >=50:
print("GRADE: C")
elif avg >=40:
print("GRADE: D")
else:
print("GRADE :E")








#creating objects
s1 =student()
s2 =student()

#User input
s1.idno =input("Enter Admin No: ")
s1.name =input("Enter Name:")
s1.course =input("Enter Course :")
s1.age =int(input("Enter Age:"))

print("\n===================\n")

print("Admin NO: ", s1.idno)
print("Name: ", s1.name)
print("Course :", s1.course)
print("Age:",s1.age)
s1.fee()
s1.grade()