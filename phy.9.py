20/3/2024
day:9
c = 0
for val in set1,set2:
    c=c+1
    if c==1:
        for element in val:
      if element not in set2:
           set3,add(element)

find the uncommon words from 2 strings
s1 = "Hellow how are you"
s2 = "hellow how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)

find the 8th fibanochi number
2)num =5
 n1 =0
 n2 =1

 for val in range(num):
     ans = n1+n2
     n1=n2
     n2 = ans
print(ans)

constructors
Eg:2
unparametrised constructor
class profile:
    def _init_(self):
        print("hellow world")

obj = profile()
obj =_init_()

Eg:3
parametarised constructor
class profile:
    def_init_(self,id,name,age):
        print(id,name,age)

obj = profile(1,"sid",29)

Eg:4
class c1:
    email ="chagvhvg@gmail.com

    def m1(self):
        name = "charan"
        place = gova
        print:(place,name)
    
    
object = c1()
object.display()

E g:5
class c1:
    def m1(self):
        name = "sid"
        age =28
        return name,age
    def display(self):
        print(name,age)
        print(self.name,self.age)
        print(self.m1())

object = c1()
object.display()


Eg:6
to use the variable inside the constructor in another methods
class class1:
    self.email = "sid@gmail.com "
    def_init_(self):
        self.name ="sid"
        self.email = "sid@gmail.com "
        return name,email

    def display(self):
        print(self,name,self,email)

     c1=class()
     c1.display()

----------->Inheritance
the process of utilising the methods and attributes of parent class
through the object of child class it is called as inheritance

types of Inheritance
single inheritance
multilevel Inheritance


single inheritance
It has aonly one parent class and only one child class
Eg:1
class parent:
    def m1():
        print("iam parent in class")

class child:(parent):
    def m2(self):
        print("iam child class")

obj = child()
obj = m1()

Eg:2
class c1:
    def __inte __(self):
        print("concontructionfrom parent class")



class child1(c1)
pass


obj =child()
        

multilevel inheritance
Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voice")

class dog (voice):
    def dog voice (self):
        print("brake")
        
class dog (dog):
    def cat voice (self):
        print("meow")
        
        
    
class parrat(cat):
    def parrot_ voice (self):
        print("speak")


all=parrot()
all.dog_voice()
all.cat_vioice()
all.sound()
all.parrot_voice()

Eg:2 
        class honda_city:
     def honda_city_engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
         print(cc, Hp, torque, fuel_type, num_of_piston)
     
     def honda_city_body_specs (self, color, weight, height, length, vehicle_type):
         print(color, weight, height, length, vehicle_type)
     
class amaze (honda_city):
      def amaze_engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
          print(cc, Hp, torque, fuel_type, num_of_piston)
     
      def amaze_body_specs(self, color, weight, height, length, vehicle_type):
          print(color, weight, height, length, vehicle_type) clace civic/amaru)

class Honda(civic):
      pass

honda=Honda()
honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
honda.civic_body_specs("white",2000,5.5,8,"Honda")

#| Multiple Inheritance ff? It has multiple parent and 1 child
class while_pertol:
      def function_w(self):
          print("used to Airplans")
         
class Organic_petrol:
      def function_o(self):
          print("used for Bike, cars")
                   
class premium petrol:
      def function_p(self):
          print("spots cars, bikes")
class petrol (while pertol, Organic_petrol, premium_petrol):
      def defanition(self):
          print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
       
calc=division()
calc.add(3,4)
calc.mul(4,2)

Heirarical inheritance
The one parent class will asct as parent for all the child classes

class catagory:
    def cat_name(self):
        print("weight")

class Tomato(catagory):
    def tomato_specs(self):
        taste="neutral taste"
        self.display(color,taste)

class carrot(catagory):
     def carrot_specs(self):
         color="green"
         taste="sweet"
         self.display(color,taste)


c=carrot()
c.carrot_specs()
c.weigth("30grms")

t=Tomato()
c.tomato_specs()
c.weigth("20grms")

Hybrid inheritance
The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")

class c2(c1):
    def m2(self):
        print("Class2")

class c3(c2):
    def m3(self):
        print("Class3")

class c4(c2):
    def m4(self):
        print("Class4")

class c5(c3):
    def m5(self):
        print("Class4")

    def m3(self):
        print("iam m3 from c4")
       
class c6(c5,c4,c2,c1):
    def m6(self):
        print("Class4")

obj=c6()
obj.m3()

------>polymorphism
 poly - many more



 ploymorphism in operators
 print(8+8)
 print("k"+'1')
 print([1,2,3,]+[5,6])

 print(6*7)
 l1 ={"k"+l}
 print(*l1)
 def f1(*args)
 l1 = [1,2,3,4]
 print(11*10)


 ploymorphism in classes
 we can achieve polymorphism in 2 ways
 1.)method overloding--->it not possible in python
 2.)method overriding

 
 





















































         










         

    































        

















              
    































        

 
     
        
        
