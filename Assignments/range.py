a = list (range(11)) #list ko range se banaya
print(a) #printing range
print(type(a)) #type of range

b = list (range(1, 11))
print(b) #printing from 1 to 10
        #    start end gap
c = list (range(1, 11, 2)) #printing from 1 to 10 with step of 2
print(c) #printing from 1 to 10

d = tuple (range(1, 11, 2)) #range in tuple
print(d) #printing from 1 to 10 with a step of 2


# range 0 se shru hota hai
#or last number chhor ke print kerti hai matlab agr 10 tk print kerwaya hai toh 0 se leke 9 tk print hoga