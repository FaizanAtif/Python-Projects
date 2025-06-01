#tuples:

a = ("apple", "banana", "cherry") #basic tuple
print(a) #basic tuple

b = tuple(("apple", "banana", "cherry")) #tuple with tuple constructor
print(b) #tuple with tuple constructor

c = ("apple",)
d = ("apple")
print(type(c)) #tuple with one element
print(type(d)) #not a tuple with one element

e = ("apple",)
f = ["banana"]

print(type(e)) #tuple with one element
print(type(f)) #not a tuple with one element

g = tuple(("apple",)) #tuple with one element
h = tuple(["banana"]) #tuple with one element
print(type(g)) #tuple with one element
print(type(h)) #tuple with one element


#tuple indexing
a = ("apple", "banana", "cherry")
print(a[0]) #first element



#tuple or list dono ki indexing 0 se start hoti hai
#or tuple mai bhi negative indexing hoti hai