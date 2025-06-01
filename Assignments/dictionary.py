#dictionary:

a = {
    "First_name": "Daim",
    "Last_name": "Imran",
    "Age": 20,
    "Country": "Pakistan",
    "hobbies": ["Coding", "Reading", "Gaming"],
    "is_married": False,
    "skills": {
        "Python": 8,
        "JavaScript": 7,
        "HTML": 9,
        "CSS": 6
    },
}
print(a) #printing dictionary
print(len(a)) #length of dictionary
print(type(a)) #type of dictionary
print(a["hobbies"]) #accessing dictionary value using key


b = dict(First_name = "Daim", Last_name = "Imran", Age = 20, Country = "Pakistan",
          hobbies = ["Coding", "Reading", "Gaming"])
print(b) #printing dictionary using dict() function
print(len(b)) #length of dictionary
print(type(b)) #type of dictionary
print(b["hobbies"]) #accessing dictionary value using key