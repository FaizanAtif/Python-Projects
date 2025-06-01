# Map and Filter in Python
#Map
a = [x for x in range(1,21)]

def add (x):
    return x + 10

new_list = list(map(add, a))

print(new_list)


#Filter
b = [x for x in range(1,21)]

def add (x):
    return x > 10

new_list = list(filter(add, b))

print(new_list)




#data set

c = [x for x in range(1,11)]
d = [x for x in range(1,11)]

def add (x,y):
    return x + y

new_list = list(map(add, c, d))

print(new_list)