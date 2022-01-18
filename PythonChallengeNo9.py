from abc import abstractmethod


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_info(): #this an abstract method
        pass

    def __del__(self):
        print("object {0} deleted".format(self.name))

class emp(person):
    def __init__(self, name, age ,salary):
        super().__init__(name, age)
        self.__salary = salary
    
    @property
    def salary(self): #getter method of __salary property
        return self.__salary
    
    @salary.setter
    def salary(self,s): #setter method of __salary property
        if s > 0 and s < 20000:
            self.__salary = 15000
        else :
            self.__salary = 25000
    
    def get_info(self):
        return  "\nname:{0}\nage:{1}\nsalary:{2}\n".format(self.name,self.age,self.__salary)

class std(person):
    def __init__(self, name, age ,level):
        super().__init__(name, age)
        self.level = level
    
    def get_info(self):
        return  "\nname:{0}\nage:{1}\nlevel:{2}\n".format(self.name,self.age,self.level)


first_emp = emp("ahmed",25,30000) #create object from emp class
first_std = std("Ala",20,4) #create object from std class

print(first_emp.get_info()) #call method get_info() to get object informations
print(first_std.get_info()) #call method get_info() to get object informations