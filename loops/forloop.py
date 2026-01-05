#For loop with List
l = [1,4,6,234,6,764]
for i in l:
    print(i)

# For loop with Tuples
t = (6,231,75,122)
for i in t:
    print(i)

#For loop with Strings
s = "Suresh"
for i in s:
    print(i)
    
# For loop else
l = [1,7,8]

for item in l:
    print(item)
else:
    print("Done") # This is printed when the loop exhausts!
    
# BREAK LOOP

for i in range(100):
    if(i == 35):
        break # Exit the loop right now
    print(i)
    
# CONTINOUS LOOP
for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)
    