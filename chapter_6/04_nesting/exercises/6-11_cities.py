cities = {
    'madinah': {
        'country': 'saudi arabia',
        'population': '1.5 million',
        'fact': 'Madinah is revered by muslims because of Holy Prophet Peace Be Upon Him.'
    },
    'makkah': {
        'country': 'saudi arabia',
        'population': '8.3 million',
        'fact': 'Muslims like Makkah because its the birth place of '
                'Holy Prophet Peace Be Upon Him.'
    },
    'baghdad': {
        'country': 'iraq',
        'population': '7.6 million',
        'fact': 'Its the city of friend of ALMIGHTY ALLAH his name '
                'is GHOSE-UL-AZAM Shiekh Abdul Qadir Jilani R.A.'
    },
}

for name, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print("\n" + name.title() + " is in " + country + ".")
    print("\t" + "It has a population about of about " + population + ".")
    print("\t" + fact)

