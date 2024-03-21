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

----->abstraction
             


       

 
    







a = 9
b = 6
print(a+b)
print(a._add_(b)) under method or mafic or mafic method


int()
print(a._sub_(b))
len()

    
        
        





























          

                  
