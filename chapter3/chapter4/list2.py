a = (1,2,3,4,5,6,7,8,9,10)
print(type(a)) #<class 'tuple'>

a = (1)
print(type(a)) #<class 'int'> #if we want to make a tuple of single element we have to add a comma after the element.

a = (1,)
print(type(a)) #<class 'tuple'>

a = (1,2,3,4,5,"suresh",True,5.67,"Shayam")
print(a)  #(1, 2, 3, 4, 5, 'suresh', True, 5.67, 'Shayam')
print(type(a)) #<class 'tuple'>