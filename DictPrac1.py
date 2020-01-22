favorite_pets = {'__Myst__': 'cats',
                 'Arun': 'dogs',
                 'horusr': 'cats',
                 'caisa64': 'cats and dogs'}
for x in favorite_pets.values():
    print(x)

print(('horusr', 'cats') in favorite_pets.items())
print(('horusr', 'dogs') in favorite_pets.items())
print('Arun' in favorite_pets.keys())
print('dogs' in favorite_pets.values())


