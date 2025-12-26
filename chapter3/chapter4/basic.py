# List and Tuples in Python
# Python lists are containers to store of values of any data type.
friends = ["Suresh", "Ramesh", "Mahesh", "Rajesh",7, True]

#str() "Suresh"  int() 7,bool() True

#list indexing 
# A list can be indexed just like a string.

L1 = [7,9,"suresh"]

L1[0] # 7
L1[1] # 9
L1[2] # "suresh"
L1[70] # IndexError: list index out of range.
L1[0:2] # [7,9] #list slicing


#List Methods.
#Consider the following list:
 
l1 = [1,8,7,2,21,15]
l1.sort() # sorts the list to [1,2,7,8,15,21]
l1.reverse() # reverses the list to [21,15,8,7,2,1]
l1.append(45) # adds 45 at the end of the list to [21,15,8,7,2,1,45]
l1.insert(3,8): # This will add at 3 index 8 to the list to [21,15,8,8,7,2,1,45]
l1.pop(2) # removes element at index 2 and return its value.
l1.remove(21) # removes 21 from the list

friends = ["Suresh", "Ramesh", "Mahesh", "Rajesh",7, True]
print = (friends[0])
friends[0] = "Suresh Kumar" #unlike strings ,list are mutable in python.

print(friends[0])
print(friends[1:4])

