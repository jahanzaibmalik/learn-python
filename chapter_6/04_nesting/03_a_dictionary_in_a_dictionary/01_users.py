# A Dictionary in a Dicitonary
users = {
    'jmalik': {
        'first': 'jahanzaib',
        'last': 'malik',
        'location': 'karachi'
    },
    'skhan': {
        'first': 'salman',
        'last': 'khan',
        'location': 'mumbai'
    }
}

for username, user_info in users.items():
    print("\nUsername :" + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



