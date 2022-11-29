import random

friends = [
    'Alexis'
    'Laura',
    'Mako',
    'Aisu',
    'Mai',
    'Genta',
    'Itsuki',
    'Lucy',
    'Jasmine',
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(friends) # randomly choose a friend

print('Who should I hangout with today?')
print(selected)