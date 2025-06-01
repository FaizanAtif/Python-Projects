def my_func(x):
    print(x)

my_func('hello faizan')


def my_func(x, y):
    print(x, y)

my_func(10, 20)



def chuchu(x, y):
    print(x + y)

chuchu(10, 20)


def faizy(x =''):
    print(x)
faizy('hello')


def faizy(x ='My name is Faizan'):
    print(x)
faizy('My name is Daim')


def faizy(*x): #infinte argument pass kerne ke liye hum name se pehle * lagate hain taake multiple argument pass ho sake
    print(x)   # single * tuple pass kerta hai or ** dictionary pass kerta hai
faizy()


def faizy(*x): 
    print(x)   
faizy(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'etc....')


def faizy(*x): 
    print(x[0])    #index ke zariye access kera maine number 1 ko
faizy(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'etc....')






def faizy(**x): #infinte argument pass kerne ke liye hum name se pehle * lagate hain taake multiple argument pass ho sake
    print(x)   # single * tuple pass kerta hai or ** dictionary pass kerta hai
faizy()


def faizy(**x): 
    print(x)   
faizy(name='faizan', age=20, city='karachi')

