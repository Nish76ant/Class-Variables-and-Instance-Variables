#Class Variable and Instance Variable

class Employee:
    no_of_leaves = 8 #Class Variables
    pass

harry = Employee()
Rohan = Employee()

harry.name = 'Harry' #Instance Variable
harry.salary = 455 #Instance Variable
harry.role = 'Instructor' #Instance Variable


Rohan.name = 'Rohan' #Instance Variable 
Rohan.salary = 455 #Instance Variable
Rohan.role = 'Student' #Instance Variable

#print(rohan.salary)
#print(harry.salary)
print(Rohan.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves = 9   #We can change class variables using only class
print(Employee.no_of_leaves)
Rohan.no_of_leaves = 14 #Instance Variable
print(Rohan.__dict__)
print(Employee.__dict__)

#we can't change the class variable using Object
#Rohan.no_of_leaves = 12---------We can't change, it will make new instance variable
#print(Rohan.no_of_leaves)

