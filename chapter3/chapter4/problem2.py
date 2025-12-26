#Write a program to accept marks of 6 student and display them in sorted manner.
student_marks = []
f1 = int(input("Enter marks of student 1:"))
f2 = int(input("Enter marks of student 2:"))
f3 = int(input("Enter marks of student 3:"))    
f4 = int(input("Enter marks of student 4:"))
f5 = int(input("Enter marks of student 5:"))
f6 = int(input("Enter marks of student 6:"))
student_marks.append(f1)
student_marks.sort()
print(student_marks)