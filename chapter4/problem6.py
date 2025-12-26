#Create an empty dictionary . Allow 4 friend to enter thair favorite language as values and use key as their names. Assume that the names are unique.
friends = {
    "Alice": "Python",
    "Suresh": "JavaScript",
    "Karan": "Java",
    "Maria": "C++",
    "Akshad": "R",
    "John": "Go"
}
print(friends)


d = {}
name = input("Enter your name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter Language name: ")
d.update({name: lang})
print(d)