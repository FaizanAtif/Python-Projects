#list methods to add n delete elements:

#append() - Adds an element at the end of the list
a = [f"A = ""apple", "banana", "cherry"]
print(a) #before append
a.append("orange")
print(a) #after append

#extend() - Add the elements of a list (or any iterable), to the end of the current list
b = [f"B = ""apple", "banana", "cherry"]
print(b) #before extend
b.extend(["orange", "mango", "grapes"]) #adding multiple elements to list
print(b) #after extend

#insert() - Adds an element at the specified position
c = [f"C = ""apple", "banana", "cherry"]
print(c) #before insert
c.insert(1, "orange") #adding element at index 1
print(c) #after insert

#remove() - Removes the first item with the specified value
d = [f"D = ""apple", "banana", "cherry"]
print(d) #before remove
d.remove("banana") #removing element from list
print(d) #after remove

#pop() - Removes the element at the specified position
e = [f"E = ""apple", "banana", "cherry"]
print(e) #before pop
e.pop(1) #removing element from list
print(e) #after pop

#clear() - Removes all the elements from the list
f = [f"F = ""apple", "banana", "cherry"]
print(f) #before clear
f.clear()  #removing all elements from list
print(f) #after clear

#delete() - Deletes the list completely
h = [f"H = ""apple", "banana", "cherry"]
print(h) #before delete
del h[2]
print(h) #after delete

#del - Deletes the list completely
g = [f"G = ""apple", "banana", "cherry"]
print(g) #before del
del g #deleting element from list
print(g) #after del