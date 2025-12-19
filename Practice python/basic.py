# What is variable ?
# A variable is a used to store data in a program.

x = 8
name = "Suresh Rana"
print(x)
print (name)

# Write a program to store and print the different data types.

a = 10   #int
b =7.5  #float
c = "Rana" #string
d = True    #bool
print(a)
print(b)
print(c)
print(d)

print(a,b,c,d)

# 3. Identify the data types of the following values.

x = 10
print (type(x)) #<class 'int'>


y = 10.5
print(type(y))  #<class 'float'>

z = "Suresh Rana"   #<class 'str'>
print(type(z))

a = True
print(type(a)) #<class 'bool'>


# Store a list and tuple in a variable and print the data types of the variables.

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)

print(my_list)
print(my_tuple)

# Swap two Variable

a = 5
b = 10

a,b = b,a
print(a,b)

# Relational (Comparison) Operators)
#Arithmetic Operators

a = 10
b = 5
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #modulus


# Relational (Comparison) Operators
# ==, !=, >, <, >=, <=

a = 10
b = 5

print(a == b) #False
print(a != b) #True
print(a > b) #True
print(a < b) #False
print(a >= b) #True
print(a <= b) #False


# Logical Operators
# and,or,not
#&&,||,!


a = 10
b = 5

print(a > b and a < b) #False
print(a > b or a < b) #True
print(not(a > b and a < b)) #True

a = True
b = False
print(a and b) #False
print (a or b)  #True
print(not a)    #False

# Assignment Operators

# =, +=, -=, *=, /=, %=, **=, //=

a = 5
a += 4
print(a) # 9


a = 5
a -= 4
print(a) #1

a = 5
a *= 4
print(a) #20

a = 5
a /= 4
print(a) #1.25

a = 5
a %= 4
print(a) #1

a = 5
a **= 4
print(a)    #625

a = 5
a //= 4
print(a) # 1.0


# Expression Example
result = (10 + 5) * 3 - 2
print(result) # 43

result1 = (45 + 4) * (5 - 7) * (8 * 7) + 45
print(result1) # -5443

# Input & Output function in Pyhthon

print("Welcome to Python Suresh Rana")

#name = input("Enter your name: ") #KumarSuresh
#print("Hello, " + name + "!")

#Input two numbers and print their sum
#a = int(input("Enter the First number:")) # any number
#b = int(input("Enter the Second number:"))# any number

#print(a + b)


#Input two numbers and print their sum
#a = float(input("Enter the First number:")) #any number
#b = float(input("Enter the Second number:"))# any number

#print(a + b)

# Formatted Output
name = "Kumar Suresh"
age = 23
height = 5.8
print("Name:",name, "Age:", age, "Height:", height)


# Formatted Output using f-string
print(f"Name: {name}, Age: {age}, Height: {height}")

marks = 85
print(f"Your marks are {marks}")



# String & String Opertors
# A string is squence of characters enclosed in single ('') or double quotes ("").
#Python provide operators like + (concatenation) and * (repetition) for string manipulation.
#and in (membership) to work with string.

a ="Python"
print(a) #Python

print("Hello" + "World") #HelloWorld
print("Hello" + "Python") # HelloPython
print("Hello" * 3) #HelloHelloHello
print("P" in "Python") #True
print("P" not in "Python") #False
print("P" not in "Java")
print("Python"[0]) #P
print(len("python")) #6

# String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # Hello World

# String Repetition
str3 = "Hi"
result = str3 * 3
print(result) # HiHiHi

# String Membership
str4 = "Hello World"
print("World" in str4) # True
print("Python" in str4) # False

# String Indexing
str5 = "Python"
print(str5[0]) # P
print(str5[1]) # y
print(str5[-1]) # n
print(str5[-2]) # o


# String Length
str6 = "Python"
print(len(str6)) # 6
print(len("Python")) # 6


# String Slicing
str7 = "Python"
print(str7[0:3]) #Pyt
print(str7[2:5]) #tho
print(str7[2:]) #thon
print(str7[:4]) #Pyth
print(str7[:]) #Python

print(str7[::2]) #Pto
print(str7[::-1]) #nohtyP


# String Methods
str8 = "Python"
print(str8.upper()) #PYTHON
print(str8.lower()) #python
print(str8.capitalize()) #Python
print(str8.title()) #Python
print(str8.swapcase()) #pYTHON
print(str8.replace("P", "J")) #Jython
print(str8.find("y")) #1
print(str8.count("y")) #1
print(str8.startswith("P")) #True
print(str8.endswith("n")) #True
print(str8.isalpha()) #True
print(str8.isdigit()) #False
print(str8.isalnum()) #True
print(str8.isspace()) #False
print(str8.istitle()) #False
print(str8.islower()) #False
print(str8.isupper()) #False

print(str8.strip()) #Python
print(str8.lstrip()) #Python
print(str8.rstrip()) #Python



# String Formatting
name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name, age)) #My name is John and I am 25 years old.
print(f"My name is {name} and I am {age} years old.") #My name is John and I am 25 years old.


# List & Tuple methods
#A list is a ordered and mutable (changeable) collection of items.
lst = [1,2,3,4,5]
print(lst) #[1,2,3,4,5]

lst.append(6)
print(lst) #[1,2,3,4,5,6]

lst.remove(1)
print(lst)#[2,3,4,5,6]

lst.insert(1,10)
print(lst) #[2,10,3,4,5,6]

lst.pop(2)
print(lst)  #[2,10,4,5,6]

lst.sort()
print(lst) #[2,4,5,6,10]

lst.reverse()
print(lst)  #[10,6,5,4,2]

lst.clear()
print(lst) #[]

#Tuple

#A tuple is a ordered and immutable (unchangeable) collection of items.
tup = (1,2,3,4,5)
print(tup) #(1,2,3,4,5)

tup.count(1) #1
tup.index(2) #1

t = (1,2,4,5,2 ,2)
print(t.count(2))   #3
print(t.index(2))   #1

# Set & Dictionary methods
#A set is a unordered and mutable (changeable) collection of unique items.
set1 = {1,2,3,4,5}
print(set1) #{1,2,3,4,5}

set1.add(6)
print(set1) #{1,2,3,4,5,6}

set1.remove(1)
print(set1) #{2,3,4,5,6}


set1.discard(2)
print(set1) #{3,4,5,6}

set1.pop()
print(set1) #{4,5,6}

set1.clear()
print(set1) #set()

set2 = {1,2,3,4,5}
set3 = {4,5,6,7,8}
print(set2.union(set3)) #{1,2,3,4,5,6

x = {1,2,3}
y = {3,4,5}
print(x & y)
