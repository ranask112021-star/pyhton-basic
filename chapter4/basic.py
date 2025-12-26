# Properties of python Dictionaries.
#1 it is a unordered collection of items.
#2 it is mutable.
#3 it is indexed.   
#4 it does not allow duplicate members.
#5 it is represented by curly braces {}.
#6 it is a collection of key:value pairs.
#7 keys must be of immutable data types (string, number, tuple).


# Dictionary Methods

a = {
    "name": "Suresh",
    "from": "India",
    "marks": [92, 85, 88]
}
print(a.keys())
print(a.values())
print(a.items())

# student Dictionary
student = {
    "name": "Suresh",
    "roll_no": 311,
    "marks":85,
    "passed": True
}
print(student)
print(student["name"]) # single value print krna 
# In english single values key.

print(student["marks"])

#  a.items(): Returns a list of (key, value) tuple pairs.
print(student.items())
#a.keys():# Returns a containing dictionary's keys.
print(student.keys())

#a.update():# Updates the dictionary with the supplid key-values pairs.
student.update({"marks": 90})
print(student)

#a.get("name"): # Returns the values of the specified keys (and values is returned  eg ,"Suresh" is returned hare).
print(student.get("name"))

# get() method (it is a safe way to access values).
print(student.get("roll_no"))
print(student.get("grade"))


# new values Add krna Dictionary me.
student["grade"] = "A"
print(student)


# Values update krna Dictionary me.
student["marks"] = 95

print(student)
# remove krna Dictionary me.
student.pop("passed")
print(student)

# Loop se print krna Dictionary me.
for k, v in student.items():
    print(k,":", v)
    
student.update({"Suersh":86, "Rahul":95})
print(student)


# get() method in python Dictionary.
# Returns the values of the given key.
# If the key does not exist , it returns None (or a default value if provided).

print(student.get("name"))
print(student.get("age", "Not Found"))# key not present in dictionary.
 

# Clear() method in python Dictionary.# clear() method in python Dictionary.
# Removes all the elements from the dictionary.

student.clear()
print(student) # Output: {}

# del keyword in python Dictionary.
# Deletes the entire dictionary.

del student
print(student) # Output: NameError: name 'student' is not defined.

# pop() method in python Dictionary.
student.pop("marks")   
print(student)
   
# copy() method in python Dictionary.
# Returns a shallow copy of the dictionary.

new_student = student.copy()
print(new_student)

# len() function in python Dictionary.
# return the number of key-value pairs.

print(len(student))



