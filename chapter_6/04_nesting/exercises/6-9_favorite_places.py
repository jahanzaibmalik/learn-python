favorite_places = {
    'jahanzaib': ['madina', 'lahore', 'baghdad'],
    'ahsan': ['karachi', 'peshawar', 'hyderabad'],
    'qasim': ['dubai', 'colombo', 'malaysia']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())