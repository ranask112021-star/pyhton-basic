# Chapter String 3
# String is a data type in python
#String is a sequence of characters enclosed in quotes.
#We can primarily write a string in these ways.
a = "Suresh" # double quotes string.
b = 'Suresh' # single quotes string.
c = '''Suresh''' # Triple quotes string.
print(a)
print(b)
print(c)

#STRING SLICING
'''
A string in python can be sliced for gretting a part of the string.

Consider the following string.

name="Suresh"=> Length of string is 6.
      012345
      S U R E S H
      -6-5-4-3-2-1
      
The index in a string starts from 0 to (Length _1) in Python. In order to slice a string .we use 
the following syntax:
s2 = name[starting_index:ending_index]

s1[0:3]return"Sur"---->characters from 0 to 3
s1[1:3]return"ur"---->characters from 1 to 3

Native include: Negative can also be used as shown in the figure above. -1
corresponds to the (length -1) index , -2 (length -2).

'''

name = "Suresh"
print(name[0:3])


#SLICING WITH SKIP VALUE

'''
We can provide a skip values as a part of our slice like this :

word = "amazing"

print(word[1:6:2])# "mzn"

Other advanced slicing techniques :

word = "amazing"
word = [:7] # word [0:7] - 'amazing'
word = [0:-3] # word [0:len(word)-3] - 'amaz'
word = [-1:len(word)-3] # word [len(word)-1:len(word)-3] - 'gn'
word = [-3:-1] # word [len(word)-3:len(word)-1] - 'zi'

'''