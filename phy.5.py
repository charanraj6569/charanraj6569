15/3/24
day:5
------> common fuctions for list
l1=[6,7,8,9,0]
print(len(l1))

print(max(l1))
print(min(l1))

l1=[6,8,9,"p","u"]
print(maxl1)


some fuctions which is specifically used for list
To addelement inside list
insert(index_value,element)---> TO add element at specific index position

to delete element from list
l1={6,6,6,7,8,9,08.89,0,-5,0]
pop(index value)--->used to delete element at specific index
l1.remove (8.89)
print(l1)

clear()---->to compleate delete all element  in list
l1.clear()
print(l1)

del --> to delete the list
del l1#or del(l1)
print(l1)


---> join 2lists

l1=[9,0,8]
l2=["p","o',"t",34]
print(l1+l2)

    or
    extend()--->to combine 2list
    l1.extend(l2)
    print(l1)

------>copy()
l1=[6,7,8,9,8]
l2=[1.copy()
    print(l1)
    print(l2)
    
print(id(l1)
print(id(l2)

! diff between shallow copy and deep copy
  shallow copy
import copy
l1=[8,9,0[5,6],[3,2,1]]
l2=copy.copy[l1]
l1.append(890)
print(l1)
print(l2)

*deep copy-->used to copy tha list with nested list
import copy
l2=copy.deepcopy(l1)
l1[-1].append('car')
print(l1)
print(l2)

sort-->arrange elements in list in ascending order
l1=[9,8,,746,4,5]


l1.sort(reverse-true)# to arrange in descending order
print(l1)
l['Z','i','o','p','g']
l1.short()
print)l1)---->error

list constructor
list()-->to convert  other collection datatype to list
l3=((8,9,0))
print(list(l3))


l4=(8,9)
print(list(14))

--->nested listl1=[8,9,[0,8,7],["P","o","y"],[8,'t']]
print(l1[-2][1]-->0


prinr(l1[1:4])
print(l1[1:-1])


to delete "t"from l1
l1[-1].remove('t')
print(l1)

combine these ["p","o","y",],[8,'t']lists in l1
l1[-2],extend(l1[-2])
      l1.pop(-1)
      print(l1)

1.)tuple have be surren by ()


Eg:
t1=(8,8,9,6,5.78,[9,0),(6,8),"hey",9+6)
print(t1)
print(type(t1))

indexing,slicing are all same as list
l1=[8]
print(type(l1))



l1=(8,)
print(type(11)) tuple

t1=8,9
print(type(l1) int

t2=8,
print(type(t2)) tuple


len(),min(),index(),count()-->all as list

to add element inside tuple--->connot add
cannot deleat any element from tuple


join 2 tuples
t1=(8,9,0)
t2=(6,7,8)
print(t1+t2)

TO add all element inside list and tuple
sum()
l1=[8,9,7,6]
print(sum(l1))

sort tuple
t1=(8,9,0,89,12)
print(tuple(sorted(t1))
print(tuple(sorted(t1,reverse=true)))

iterate list and tuple
for i in l1:
      prinr(i)
      
l1=[9,8,9,8,0,9]
for i  in range(0,lan(l1))
     print(l1[1])

----------->strings
s1='o'
print(type(s1))

s1="hello world"
To access string
print(s1)
indexing and slicing-->same as list and tuple
print(s1[0:5])

--->comaon fuctions

len(),min(),max(),index(),count()
s1="hellow world"
print(len(s1))
print(max(s1))
print(min(s1))



title()
s1='never giveup'
print(s1.title())

capitalize()----->1st char of string will be converted to capital
s1='never giveup'
print(s1.capitalize())

join the strings
s1="hellow"
s2="world"
print(s1+s2)

s1='''
how are you
i am fine
hey there
'''

spilines ()----->used to split the string based on lines
print(s1.splitlines())

find()---->to find the index based on a cherecter
s1="hellow world"
print(s1.find('h')
print(s1.index('h')

join()---->
l1=["hey","there"]
print("".join ())
print("$".join())

s1="welcome to all"
print(s1.endswitch('l'))
print(s1.startswitch('w'))


s1="67"
print(type(s1))
print(s1.isdigit())

print the string in reversemanner
s1="welcome to all"
print(s1[::-1])


---->Eg:1
wap to find the number of lower case letters
s1 ="hey three you are"
for i in s1:
      print(i)
      
      
s1 ="hey three you are"
count=0
for i in s1:
    if i.islower():
        count+=1
print("the total num of lower case letters:",count)        
      
s1='restarter'
s1= "imagin"
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst,"$"))
print(fst+txt)

      
Eg:3
s1="charanraj"
for val in s1:
    print(val)

cherecters=len(s1)
print(charecters)

words=s1.split("")
print(len(words))

             
sentenses=s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))        

for val in s1:
    if val ==" ":
        print(True)

               

               

      


      
      
      
      



      
      
      









      



      
      
      
      
      
      
      
      
    































      
      
      
      
      
      
      
      

      
      
      

      
      
      
      
      
      
      
      

      
      
      
      
      
      
      
      
      

      
      















      























      


























      















































      






































      


























      
      




























      





































      
