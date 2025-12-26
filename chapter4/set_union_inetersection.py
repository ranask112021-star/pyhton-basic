s1 = {1,45,6,78}
s2 = {7,8,1,78}
print(s1.union(s2))# Union of two sets.Output: {1, 6, 7, 8, 45, 78}
print(s1.intersection(s2))# {1, 78} # Intersection of two sets.
print(s1.difference(s2)) # {45, 6} # Difference of two sets.
print(s1.symmetric_difference(s2)) # {6, 7, 8, 45} # Symmetric difference of two sets.
print(s1.issubset(s2)) # False # Check if s1 is a subset of s2.
print(s1.issuperset(s2)) # False # Check if s1 is a superset of s2.
print(s1.isdisjoint(s2)) # False # Check if s1 and s2 are disjoint.
print(s1.clear()) # None # Clear all elements from s1.
print(s1.copy()) # {1, 45, 6, 78} # Copy of s1.
print(s1.pop()) # 1 # Remove and return an arbitrary element from s1.
print(s1.remove(45)) # None # Remove 45 from s1.
print(s1.discard(6)) # None # Remove 6 from s1 if it is present.
print(s1.add(100)) # None # Add 100 to s1.
print(s1.update({200,300})) # None # Update s1 with elements from another set.

print(s1) # Final state of s1 after all operations.


