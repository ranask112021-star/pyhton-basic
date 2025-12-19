#Write a python program to print the content of a directory using the os module.import os
import os
# Directory path (current directory)
path = "/"

# List all files and folders
for item in os.listdir(path):
    print(item)

#list all full path also
import os

path = "D:/python1"

for item in os.listdir(path):
    full_path = os.path.join(path, item)
    print(full_path)
