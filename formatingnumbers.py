#user input- int
oop1 =int(input("Enter OOP 1 Marks:"))
oop2 =int(input("Enter OOP 2 Marks:"))
dbms =int(input("Enter DBMS Marks:"))

total = oop1+oop2+dbms
avg =total/3

print("\n================\n")
print("OOP1 Marks:", oop1)
print("OOP2 Marks:", oop2)
print("DBMS Marks:", dbms)
print("Total:", total)
print("Average:%.2f" %avg)

if avg >=70:
   print("GRADE : A")
elif avg >=60:
   print("GRADE : B")
elif avg >=50:
   print("GRADE : C")
elif avg >=40:
   print("GRADE : D")
else:
   print("GRADE: E")