character = input("Enter the name of a game character: ")
weapon = input("Enter a type of weapon: ")
place = input("Enter a fantasy place: ")
emotion = input("Enter an emotion: ")
adjective = input("Enter an adjective: ")
battle_cry = input("Enter a battle cry: ")

madlib = (
    f"{character} raised their {weapon} high and charged into the heart of {place}. "
    f"With a face full of {emotion} and a {adjective} spirit, they shouted '{battle_cry.upper()}!' "
    "The enemies trembled as the ultimate showdown began."
)

print(madlib)
