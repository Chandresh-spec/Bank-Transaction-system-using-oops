# # encapsulation->wrapping data+methods together and controlling acces
# # 
# # public method

# # 1️⃣ Public Members
# # ✅ Definition
# # 
# # Accessible everywhere
# # 
# # No underscore




# class Student:
#     def __init__(self):
#         self.name="chandresh"




# s1=Student()
# print(s1.__hash__)



# # protected members


# class Bank:
#     def __init__(self):
#         self._bal=0
    

#     def post(self):
#         self._bal+=30
#         print(self._bal)





# p1=Bank()
# print(p1._bal)
# p1.post()
# print(p1.__hash__)






# # private member


# class Canara:
#     def __init__(self):
#         self.__cid="123"
#         self._id="456"





# c1=Canara()
# print(c1._Canara__cid)

# print(c1.__hash__)




# class BankAccount:
    # def __init__(self):
        # self._bal=0
        # self.__accnum="123"
# 
# 
    # def deposit(self,amt):
        # if amt >=100:
            # self._bal+=amt
            # print(f"amount of {amt} is added to ur account your balance is",)
            # self.get_balance()
# 
        # else:
            # print("amt should be greater than 100")
# 
        # 
        # 
    # 
    # def withdraw(self,amt):
        # if self._bal>=amt and amt>=100:
            # self._bal-=amt
            # self.get_balance()
        # elif self._bal<amt:
            # print("insufficient balance")
        # else:
            # print("amt should be greater than 100")
# 
    # 
# 
    # def get_balance(self):
# 
        #   print(f"ur balance is {self._bal}")
        # 
        # 
    # 
    # 
# 
# 
# 
# 
# 
# p1=BankAccount()
# p1.deposit(1000)
# p1.withdraw(200)





class Bank:
    def __init__(self):
        self.__num=0
    

    def print_num(self):
        print(self.__num)




class Student(Bank):
    def __init__(self):
        self.data=0





s=Student()
s.print_num()

    