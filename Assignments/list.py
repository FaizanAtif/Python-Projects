#List
a = ["faizan", 40, 4.5, True]


# index
#    0  1  2  3  4
b = [1, 2, 3, 4, 5] # number list
#   -5 -4 -3 -2 -1
#negative Index


# index
#     0    1    2    3    4
c = ["a", "b", "c", "d", "e"] #string list
#    -5   -4   -3   -2   -1
#negative Index




#List with Constructor
d = list (("faizy", "daim", "chuchu"))


e = d.copy() #to copy any list to any other variable

print(e)


print(len(b)) #b ki length

print(type(b)) # b ki type

#To access any code with index
print(b[2]) #maine 3 ko access kiya hai
print(b[-3]) #negative indexing ke zariye 3 ko access kiya hai


#Slicing of List
print(c[0:3])  #maine 0 se leke 3 index ko access kiya yani a b c ko or 3 wala index print nahi hoga ismai 2 tk hoga
print(c[-5:-2]) #negative negative indexing se a b c ko access kiya hai

# Index Jumping
print(c[0:5:2]) #aik ko chhor kr aik data show kerega yani a c e
print (c[0:5:3]) #ismai ye 3rd index pe jump kr ke shoe karayega yani a d


#kisi bhi index ko replace kerne ka tareeka
a[3] = "z"  #maine true ko z se replace keraa a variable mai
print(a)

a[0:2] = ["Faizy", "daim"]
print(a)