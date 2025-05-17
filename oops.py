# class Car:
#     def __init__(self,brand):
#         self.brand = brand


#     def drive(self):
#         print(f"{self.brand} is driving")

# car1 =  Car('toyota')
# car1.drive()


# # encapsulation
# class person:
#     def __init__(self,name,l_name):
#         self.__name = name
#         self.l_name = l_name


#     def get_name(self):
#         return self.__name self.l_name


# p = person("Ali","ajmal")          
# print(p.get_name())


# # inheritance
# class Animal:
#     def cat(self):
#         print("this is cat")

# class Dog(Animal):
#     def bark(self):
#         print("dog barks")   


# d = Dog()        
# d.cat()
# d.bark()


# # polymorpizam

# class Brid:
#     def sound(self):
#         print("some bird sound")

# class Parrot(Brid):
#     def sound(self):
#         super().sound()
#         print("parrot say hello")


# obj = Parrot()        
# obj.sound()


# # abstaact

# from abc import  ABC , abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")       
# d = Dog()
# d.sound()






# class person():
#     def namee(self):
#         self.name = "ali"
#         return self.name

# n = person()
# print(n.namee())




# # constucter
# class person():
#     def __init__(self,name,age,salry):
#         self.name  = name
#         self.age = age
#         self.salry =  salry


# n = person("ali",29,29000)
# print(f"{n.name} ,{n.age} , {n.salry}")


# # inharitance
# # single
# class A:
#     def displayA(self):
#         print("Display  A")

# class B(A):
#     def displayB(self):
#         print("Display B")


# inharits =  B()     
# inharits.displayA()
# inharits.displayB()


# # inharits multy

# class A:
#     def displayA(self):
#         print("Display A")

# class B:
#     def displayB(self):
#         print("Display B") 

# class C(A,B):
#     def displayC(self):
#         print("Display C")

# d = C()        
# d.displayA()
# d.displayB()
# d.displayC()



# # Encupsulation

# class Encap:
#     def __init__(self,name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

# e = Encap("akmal")   
# print(e.get_name()   )  



# # polymorhiman
# class poly:
#     def sound(self):
#         print("AAAA")

# class mor(poly):
#     def sound(self):
#         super().sound()
#         print("BBB")   

# p = mor()
# p.sound()


# # abstract

# form ABC import @abstractmethod

# class abstractsa(ABC):
#     @abstractmethod
#     def abd(self):
#         pass
#     def stric(self):
#         print("abstriction")
# a = abstractsa()
# a.abd()
# a.stric()



class student:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
    def __str__(self):
        return f"Name: {self.name},Age: {self.age}"
s = student("ali",3)
print(s)
