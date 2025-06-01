#List methos sort and reverse

# The sort() method sorts the list ascending by default, 
# and the reverse() method reverses the elements of the list in place.

#Sort
a = ["banana", "apple", "cherry"]
print(a) #before sort
a.sort() #sorting list
print(a) #after sort

#Reverse
b = ["apple", "banana", "cherry"]
print(b) #before reverse
b.reverse() #reversing list
print(b) #after reverse

c = ["apple", "banana", "cherry", "apple"]
d = c.count("apple") #counting element in list
print(d) #after count

e =list ((1, 2, 3)) #creating list from tuple
print(*e) #star ka sign lagane se print mai bracket nhi dikhayega
