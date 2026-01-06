class Person:
    def __init__(self,name,id_no,role):
        self.name=name
        self.id_no=id_no
        self.role=role

    
    def get_details(self):
        return f"{self.name}  and id ={self.id_no} and role is {self.role}"
    


    def get_role(self):
        return f" role = {self.role}"
    



class Student(Person):
    def __init__(self,course,year,role,id_no,name):
        self.course=course
        self.year=year
        super().__init__(name,id_no,role)
    

    def study(self):
        return f" mis or mr is studying in {self.year} in {self.course}"
    



class Teacher(Person):
    def __init__(self,sub,sal,name,id_no,role):
        self.sub=sub
        self.sal=sal
        super().__init__(name,id_no,role)
        

        
    
 
    def teach(self):
        return f" miss/mrs will teach {self.sub} subject"
    

class HOD(Teacher):
    def __init__(self,dep,sub,sal,name,id_no,role):
        self.dep=dep
        super().__init__(sub,sal,name,id_no,role)


    def conduct_meeting(self):
        print("today has meeting")


s1=Student("BCA","2","student","2607","chandresh")
print(s1.get_details())
print(s1.study())


t1 = Teacher("Python", 50000,"anisha","101","teacher")
print(t1.get_details())
print(t1.teach())






    
        
    