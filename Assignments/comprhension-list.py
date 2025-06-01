num=[]
for i in range(11):
    num.append(i)
print(num)



# This is the same as:
num = [i for i in range(1,11)]
print(num)

name = [i for i in range(1,11)]

if 10 in name:
    print('yes')
else: 
     print('no')