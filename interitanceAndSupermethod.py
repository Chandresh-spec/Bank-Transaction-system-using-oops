# class College:
#     def __init__(self,name,rno):
#         self.name=name
#         self.rno=rno


#     def print_name(self):
#         return self.name
    
#     def roll_no(self):
#         return self.rno
    




# class Student(College):
#     def __init__(self,cls,rno,name):
#         self.cls=cls
#         super().__init__(name,rno)






# s1=Student("3bca","chandresh",123)
# print(s1.cls)


# print(s1.__dict__)

# print(s1.print_name())

    


# 
# override+super().method


# class Canara:
#     def __init__(self,nmbr):
#         self.nmbr=nmbr
#     def stinfo(self):

#         print(f"students number are{self.nmbr}")


    
# class Student(Canara):
#     def __init__(self,name,nmbr):
#         super().__init__(nmbr)
#         self.name=name




# s1=Student("chandresh",101)
# print(Student.mro())
# s1.stinfo()



    


# method overide


class BCA1:
    def num_of_st(self):
        print("student number are 100")



class Canara(BCA1):
    def num_of_st(self):
        super().num_of_st()
        print("number of student are 300")





c1=Canara()
c1.num_of_st()
