a = ['a','b', 'c', 'd']
b =enumerate(a)

print(list(b)) #printing enumerate object

for i in enumerate(a):
    print(i) #printing enumerate object

for i in enumerate(a, start=1):
    print(i) #printing enumerate object
#enumerate object is iterable

#enumerate object is iterable