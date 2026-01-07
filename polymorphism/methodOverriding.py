class Bank:
    def pay(self):
        print("parent class")




class Student(Bank):
    def pay(self):
        print("child")





s1=Student()
s1.pay()




class Calculator:
    def __init__(self,op1,op2):
        self.op1=op1
        self.op2=op2



    def __add__(self):
        print(self.op1+self.op2)




c1=Calculator(10,20)
c2=Calculator(20,30)

print(c1+c2)

