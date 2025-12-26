friends = ["Apple","Orange",5,345.06,"Akshad","Suresh"]
print(friends)

friends.append("Sachin")
print(friends)

list1 = [1,5,3,9,7]
list1.sort()
print(list1)
list1.reverse()
print(list1)

list1.insert(2,25)
print(list1) # insert 25 such that its index in the list is 2.
list1.pop(4)
print(list1) # removes element at index 4

print(list1.pop(4)) # removes element at index 4 and return its value.
list1.remove(25)
print(list1) # removes 25 from the list