people = []

person = {
    'first_name': 'ahsan',
    'last_name': 'ali',
    'age': 20,
    'city': 'karachi'
}
people.append(person)

person = {
    'first_name': 'jahanzaib',
    'last_name': 'malik',
    'age': 30,
    'city': 'karachi'
}
people.append(person)

person = {
    'first_name': 'qasim',
    'last_name': 'ali',
    'age': 32,
    'city': 'karachi'
}
people.append(person)

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    city = person['city'].title()
    age = str(person['age'])

    print(full_name + ", of " + city + ", is " + age + " years old.")