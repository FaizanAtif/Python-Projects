a =['a', 'b','c', 'd']
b = ['e', 'f', 'g', 'h']

# append
a.append('e')  #kisi bhi cheez ko add kerne ke liye list mai
print(a)  # ['a', 'b', 'c', 'd', 'e']
a.append(b)  #yaha maine poora list uta ke list ke guserdiya hai lekin kharab method hai ye
print(a)  # ['a', 'b', 'c', 'd', 'e']

# extend
a.extend(b) # kisi bhi list ko dusri list mai add kerne ke liye
print(a)  # ['a', 'b', 'c', 'd', 'e', 'e', 'f', 'g', 'h']

# remove
a.remove('e') # kisi bhi cheez ko list se remove kerne ke liye
print(a)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# del
del a[0] # kisi bhi cheez ko list se delete kerne ke liye index number ke zariye
print(a)  # ['b', 'c', 'd', 'e', 'f', 'g', 'h']