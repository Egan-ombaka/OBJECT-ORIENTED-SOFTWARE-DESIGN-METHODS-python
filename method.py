#create class

class student:
    #attributes
    idno =""
    name =""
    course =""
    age =0

    #mmethod
    def fee(self) :
        amount = float(input("Enter the amount to be paid : "))
        amountpaid = float(input("Enter the amount paid : "))
        balance = amount - amountpaid

        print("\n============")

        print("Balance : ", balance)
#creating objects
student1 =student()
student2 =student()