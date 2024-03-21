21/3/2024
day:10
 method of over_riding
 ploymorphism in classes

 class bank:
     def ratio(self):
         print("all bank has repo rate")

 class SBI (bank):
     def ratio(self):
         print("SBI RATE IS 9%")

 class IOB(bank):
     def ratio(self):
         print("IOB RATE IS 7.5")

i=IOB()
i=.ratio()

s=SBI()
S.ratio


Eg:2
class USA:
    def language(self):
        print("english")


     def capital(self):
         print("washington dc")


     class India(USA):
         def language(self):
             print("NONE")

      def capital(self):
          print("NEW delhi")


I=india
I.language()
I.capital()

EG:3

polymorphism using objects


c1,c2--------->c1=print(c10,print(c2)
f1,f2

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1=c2()
obj1.f1()

obj2=c1()
obj.f1()

Eg:4
class c1:
    def f1(self):
       print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1=c2()
obj2=c1()

def display(a)
    a.f1()

display(obj1)
display(obj2)

changing the functionliy of builtin functions
class shopping:
    def item_list(self,l1):
    items=len(l1)
    print(items)

s=shopping()
print(len(s))


a=9
b=6
print(a+B)
print(a._add_(b)) under method or mafic method

int()
print(a._sub_(b))
len()

#!------>method overloding
class suming:
    def add (self,a,b):
        print(a+b)


   def add (self,a,b,c):
       print(a+b+c)


s =suming()
s.add(4,5)
s.add(4,5,1)


EG:2
class summing:
    def add(self,a=None,b=None):
        if a!=NOne and b!=None and c!=None
        print(a+b+c)
     elif a!=None and b!=NOne:
         print(a+b)
         else:
             print(a)

obj=summing()
obj.add(2)
obj.add(3,4)
obj.ad(1,2,3)

----->abstract             
a = 9
b = 6
print(a+b)
print(a._add_(b)) under method or mafic or mafic method


int()
print(a._sub_(b))
len()

---->Abstraction
Tha process of hiding the implimentation details is abstrction









Eg:2
super()----->used to access the perent class method
from abc import ABC, abtractmethod
class c1(ABC):
    @abtractmethod
    def m1(self)
    print ("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iamchild 1")

def m1(self):
    pass
class2= c2()
class2.m2()
        
Eg:3
from abc impact ABC,abstractmethod
class password(ABC):
    @abstractmethid
    pswd="charan6565"

class login:
    def validata(self,name,password):
        if super().pwd()==passwrd:
            print("welcome",name,'!!!')
            print("login successfull")
          else:
              print("please check the passwork")

      def PWd(self):
          pass

login=login()
name= input("enter thename:")
pwd=input("enter the password:")
login.validata(name,Pwd)

#! Encapsulation

Eg:1
class car:
    name="BMW" # private variable

C1 =CAR()
print(c1.name)
c1.name = "Audi"
print(c1.name)
    
------>Eg:2
accessing private data outside the class
class c1:
    _phone = '54635654'

    def dispaly (self):
        print(self._phone)

c =c1()
c.display()

----->Eg:3
declere private method
class class1:
    def m1(self):# private method
        print("Iam private method")

c=class()
c.m1()  error

nested class
class class1:
    class class2:
        name = "cjhar"


        def display(self):
            print(self.name)
obj1=class2()

obj=class()
obj.obj.display()

----->tasks
write code for the below task using fuction
1.) d1 = {"shirt":1000,"part":1500,"shoes":"900","handkey":30}
            
        
    
    
    



















    
        
        





























          

                  
