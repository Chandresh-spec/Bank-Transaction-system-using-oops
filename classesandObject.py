class Student:
    def __init__(self,name):
        self.name=name

    

    def post(self,data):
        return data
    




s1=Student("chandresh")
print(s1.post("moger"))
        


s2=Student("moger")
print(s2.post("moger"))



# how memory will occupied


# when i created student class it is blueprint for building objects
# objects will use this blueprint

# object?
# 
# object is real instance created form the class

# object will occupy the memory




# where data is stored?
# inside the class ->no
# inside the object -> yes




# each object has a dictionary


# u1.__dict__

# u1 → { name: "A", email: "a@gmail.com" }
# u2 → { name: "B", email: "b@gmail.com" }
# 




# __init__  (constructor)-> it runs automatically when a object is called





# when i created the object 

# s1=Student("chandresh")

# python internally convert this to


# User.__init__(u1, "A", "a@gmail.com")



# instance method

# 
# s1.post(100)
# 
# 


class Bank:
    def __init__(self,bal,accnum):
        self.bal=bal
        self.accnum=accnum


    
    def balance(self):
        print(self.bal )
        print(self.accnum)
    


    def deposit(self,amt):
        self.bal+=amt

        print(f"{amt} added sucessfully",self.bal)
    

    def withdraw(self,amt):
        self.bal-=amt

        print(f"{amt} withdarw form your account",self.bal)


    


p1=Bank(500,"123456")

p1.balance()
p1.deposit(500)
p1.withdraw(200)

print(p1.__dict__)