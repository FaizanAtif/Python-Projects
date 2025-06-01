userName = input('Enter your name: ')
age = int(input('Enter your age: '))
gender = input('Enter Ur Gender:')


if userName == 'faizan' or 'faizan atif':
    print ('WELCOME FAIZAN!')
    if age >= 18 or age <= 60:
        print ('YOU ARE ELIGIBLE TO VOTE')
    elif gender == 'male' or 'Female':
        print("Thanks for telling ur Gemnder")
    else:
        print ('YOU ARE NOT ELIGIBLE TO VOTE')
