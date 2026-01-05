'''
# Chapter 7
# Sometimes we want to reapeat a set of statement in our program. for instance : Print1 to 1000.
#Loops make it easy for a programmer to tell the computer whitch set of instruction to repeat and how!
# Types of loops in python
# Primarily there are two types of loops in python .
# . While loop
# . for loops

# We will look into these one by one.
'''
for i in range(1, 6):
    print(i)

# For loop 
# A for loop is used to iterate throught a sequence like list ,tuple ,or String[Iterable]
#Syntax

'''
l = [1,7,8]
for item in l:
    print(item) # print 1,7 and 8
    
#  Range Function In Python 
The range {} function in python is used to genrate a sequence of number .

We can also specipy the start , stop and step-size as follow:

range(start,stop,step-size)
# step size is usually not used with range()

An Example Demonstrating range() function.

for i in range(0, 7): #range (7)can also be range()
    print(i) # print 0 to 6
    
# For loop with else
A optinal else can be used with a for loop if the code is to be executed when the loops exhausts.



THE BREAK STATEMENT
'break' is used to come of the loop when encounterd . it instructs is the program to exit the loop now

for i in range (0,80):
    print(i)# this will print 0,1,2 and 3

    if i == 3
        break
        
THE CONTINOUS STATEMENT
'continous' is used to stop the current iteration of the loop and continous with the next one. It instruct the Program to "skip this iteration".
for i in range(4):
    print

'''