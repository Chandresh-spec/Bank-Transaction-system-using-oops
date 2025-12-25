# encapsulation->wrapping data+methods together and controlling acces
# 
# public method

# 1️⃣ Public Members
# ✅ Definition
# 
# Accessible everywhere
# 
# No underscore




class Student:
    def __init__(self):
        self.name="chandresh"




s1=Student()
print(s1.__hash__)



# private members


class Bank:
    def __init__(self):
        self._bal=0
    

    def post(self):
        self._bal+=30
        print(self._bal)





p1=Bank()
print(p1._bal)
p1.post()
print(p1.__hash__)