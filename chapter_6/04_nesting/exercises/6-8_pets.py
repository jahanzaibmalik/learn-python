pets = []

dog = {
    'owner': 'mark',
    'animal type': 'dog',
    'name': 'dogy',
    'kind': 'bulldog',
    'eat': 'meat'
}
pets.append(dog)

cat = {
    'owner': 'sarah',
    'animal type': 'cat',
    'name': 'ragy',
    'kind': 'ragdoll',
    'eat': 'fish flakes'
}
pets.append(cat)

parrot = {
    'owner': 'jahanzaib',
    'animal type': 'parrot',
    'name': 'mithu',
    'kind': 'eclectus',
    'eat': 'seeds, vegetables, fruits'
}
pets.append(parrot)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, pets_info in pet.items():
        print("\t" + key + ": " + pets_info)
