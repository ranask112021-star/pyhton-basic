#write a program to detect double spaces in a string.

name = "Suresh is a good boy and"

print(name.find("  "))
print(name.replace("  "," "))
print(name) # String are immutable which means thats you cannot change them by running functions on them.
