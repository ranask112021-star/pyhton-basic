s = {1,5,32,54,5,5, "Shivang"}
print(s,type(s)) #{32, 1, 5, 54, 'Shivang'} <class 'set'>.
# set me duplicate values allowed nhi hote.
# set is unordered collection of items.
# set me indexing nhi hoti.
# set me mutable nhi hota.
# set me list nhi bana sakte.
# set me dictionary nhi bana sakte.
# set me tuple bana sakte hai.  

s.add(100) # set me new value add krna.
print(s ,type(s))

# Properties of set:
#1 it is an unordered  => Elements order does not matter
#2 it is an unindexed => Cannot access elements by index
#3 there is no way to change items in sets
#4 sets cannot contain duplicate values

# Operations on sets:
#Consider the following set:
s1 = {1, 2, 3, 8, 4, 5}
print(s1)
s1.remove(3) # remove() method to remove an item from a set.
print(s1)
s1.discard(4) # discard() method to remove an item from a set.
print(s1)   
s1.pop() # pop() method to remove and return an arbitrary item from the set.
print(s1)

s1.clear() # clear() method to remove all items from the set.
print(s1)   