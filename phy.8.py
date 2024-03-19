19/03/2024
day:8
def profile(name)
print(name)
profile("charan")


def profile(age)
 print(age)
 profile("45")

def profile(name,age,place):
    txt = "my name is {}. Iam {} years old Iam from{}"
    print(txt.formate(name,age,place))
    profile("sid",29,"cbe")
    
Eg:4
function with return statement

def f1():
    z=8
f1()
print(z) error --->cannot use outside the fuction

def f1(a,b):
    c=a*b
    return c
print (f1(6,8))
obj=f1(6,8)
obj1=f1(6,8)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

123
print(123)


def profile(name,age,place):
    txt = "my name is {}. Iam {} years old Iam from{}"
    print(txt.formate(name,age,place))
    profile("sid",29,"cbe")
    

positional arges
keyword args
default arge
variable length arge
keyword variable length arge

position arges
Eg:1
def profile(name,phone,mark):
    txt = "my name is{}. my phone number is {}. i got {}. marks."
    print(txt.format(name,phone,mark))

profile(546565654654654, "vhgvjhgv",97)


default args
Eg:1
def profile(name,phone,mark):
    txt = "my name is{}. my phone number is {}. i am from{}."
    print(txt.format(name,place,phone))


profile("sid,uytuyty")
    


def profile(name,phone,mark):
    if place =="kadapa" or place =="kadapa" or "kadapa":
    txt = "my name is{}. my phone number is {}. i am from{}."
    print(txt.format(name,place,phone))
 else:
     print("you are not sigup")
 file("charan",93718293)
 
variable length params
Eg:1
To pass more then 1arg to a parameter means use veriable length args
To convert normal parameter to variable length param ,add *to perfix ofprint

def profile(*name):
    print("my name is",name)
profile("cha",'name2','name3')    
    
name = "cha","name1","name2"
for val in name:
    print("my name is"val)
profile("char",'name2')    

Eg:2
def profile(*name):
for val in name:
    print("my name is",val,"my age is",age)
profile(28,"sid",'name2','name3')

keyword variable length args
kwargs --->which is used to provide the args in the from of key value pair.
Eg:1
def price(price_list):
    price(price_list)

print(shirt=1000,iphone=80000)
    
    
n=5
{1:1,2:4,3:9,4:16,5:25}

d1 = {"a":100,"b":200,c=300}
d1=dict(a=100,b=200,c=300)
print(d1)

n=5
{1:1,2:4,3:9,4:16,5:25}

n=int(input("Enter the number:"))
d1={}
for val in range(1,n+1):
    d1[val]=val**2
    print(d1)
   
def dict1(n):
    d1={}
for val in range(1,n+1):
    d1[val]=val**2
    print(d1)
dict1(5)

--->object oriented programming
The paradigms of objects oriented programming are

class
objects
inheritance
polymorphism
abstraction
encaosulation
#! class is a blue print of an object
l1 = [1,2,3,4,5,6]

Eg:1
class c1:
    name = "vinay"
    print(name1)

Eg:2
class person:
    name="vinay"

c = person() c os object
the process of created with aclass is called as Instantion
print(c.name)
    
Eg:3
create of a method
when the function is createad with a class is called as method


method with out parameter
class person:
    def display(persone):it is a method
    print("hellow welcome to class")

p=person()
p.display()

Eg:4
method with  parameter
class person:
    def display(persone,name,age)
    print(name,age)

p=person()
p.display("charan",20)


Eg:5
class person:
    name = "char" attribute or static variable

    def display(person):
    print(name3)

p = pewson()
p.display()



class person:
    fname = "char"
    lname ="T"


def first_name(self):
    print(self.fname)

def full_name(self):
    print(self.fname+""+self.lname)

p = persone1()
p.first_name()
p.full_name()

Eg:6
constructors--->_init()
this is a special method which has the ability to execute iotself without
calling it manullay through the process of instantiation

class profile:
    def d1(self):
        print("hey")

p = profile()
p.d1()
        
    





























    


    
    







    
    














































































    
    

    
