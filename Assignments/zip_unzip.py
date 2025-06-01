name = ["faizan", "ali", "ahmed", "saad"]
age = (20, 21, 22, 23)
players = ["p1", "p2", "p3", "p4"]

# Zipping
zip_list = list(zip(players, name, age))
print(zip_list)

#zipping in Tuple
zip_list1 = tuple(zip(players, name, age))
print(zip_list1)


# Zipping in Dictionary
zip_list2 = dict(zip(players, name))
print(zip_list2)  #dict ko use kerne ke liye saare tuple ya saare list hone chayie werna error ayega


# name1 = ["faizan", "ali"]
# age1 = (20, 21, 22)
# players1 = ["p1", "p2", "p3"]

# zip_list3 = list(zip(players, name, age))
# print(zip_list3)   

#ZIP KERNE KE LIYE SAB KI VALUE SAME HONI CHAYIE MATLAB PLAYER MAI BHI 3
#AGE MAI BHI 3 OR NAME MAI BHI 3 HONI CHAYIE VALUE WERNA ERROR AAYEGA


# Unzipping

zip_list = list(zip(players, name, age))

for x in zip_list:
    game_player, player_name, player_age = x
    print(player_name)

