18/03/2024
day:7
set1 = {'python','java','Data science'}
set2 = {'ML','AI','R Language','Python'}
set3 = {'Data Analytics','Robotics','Deep Learning'}
c = 0
for val in range(3):
    c=c+1
    if c==1:
       for val in set1:
           if val in set2 or val in set3:
            flag=1
            break
       
    if c==2:
       for val in set2:
           if val in set1 or val in set3:
              flag=1
              break
                         
    if c==3:
       for val in set3:
           if val in set2 or val in set1:
              flag=1
              break
            if flag==0:
   print("Disjoint")

else:
   print("Disjoint")


list = ["m","na","i","ke"]
list = ["y","me","s","lly"]

l3=[]
for val in range (len(list1)):
    ans = list1[val]+list2[val]
    l3.appende(ans)
print(l3)

i=0
while i<len(list1):
    l3.appende(list[i]+list[i])
    i+1
print(l3)

#! fuctions
DEF
function is a block of code which is is used to perform a specific fuctionalisty
functions can be created using def keyword


function has 3 parts
function  decleration
function defanition
function call

Eg:1
def greet():# function defanition
    print("welcome user!!")

greet()
greet()
greet()#fuction calling



Eg:2
function whith parameter
def greeting(name):
    print ("welcome",name)

for val in rang (3):
    username = input("enter the name:")
    greeting(username) # user name is argument


    
    

























    


    
