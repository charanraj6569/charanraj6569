14/3/2024
day:4

---->while loop
---->break using while loop

Eg:1
Iterate from 20 to 30 and break the loop in 27
i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1

Eg:2
i=20
while i<31:
    if i==27:
        break
    i+=1



 i=20
 while i<31:
     if i==27:
         break
        print(i)
        i+=1

    Eg:4
    i=20
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)

for row in range(0,6):
    for col in range(0,6):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
          print("*", end= " ")
        else:
            print(" ",end=" ")
    print()


    
while to iterate from   12 to 22 find the sum of a


Eg:5
i=12
while i<22:
    i=i+1
    print(i)


i=12
sum=0
while i<22:
    sum=sum+i
    print(sum)
    i=i+1
    
  i=12
sum=0
while i<22:
        print(i)
        sum=sum+sum
        i+=i


find average of value of 20 to 25


i=20
avg=0
while i<25:
print(avg)


i=20
avg=0
while i<25:
     i+=1
 print(avg)
i=2 




i=20
sum=0
while i<26:
    sum=sum+i
    i+=1
    print(sum/6)




i = 20
sum = 0
count = 0
while i<=26:
    sum=sum+i
    count+=1
    i+=1
    print(sum/count)


for row in range(rows):
    for col in range(cols):
        print("*", end= " *)
    print()

sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum, end= " ")
    print()




sum=0
for row in range(0,6):
    for col in range(0,6):
        sum=sum+1
        print(sum, end= " ")
    print()


for row in range(0,6):
    for col in range(0,row+1):
        print("*", end= " ")
    print()


for row in range(0,6):
    for col in range(row+1,6):
        print("*", end= " ")
    print()


for row in range(0,6):
    for col in range(row+1,6):
        print("*", end= " ")
    print()

------>datatypes
pprimary


number ----->int,flot complex
string
Boolean
none



collection
list
tuple
set
dictionary


l1 = [1, 4, 1, 7,89.7,7.5,"p","i"]
print(l1[0])
print(l1[4])
print(l1[20])-- > error



lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(l1=[-1])
print(l1=[-5])      


lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(l1[-4:-1])
print(l1[-1:-4]) --> []

lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(l1[-4:-1])
print(l1[-1:-4]) --> []


l1 =[9,8,0,6]
l1 .append("car")
print(l1)

    
  




    


