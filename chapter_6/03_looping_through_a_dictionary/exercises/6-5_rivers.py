rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'amazon river': 'south america'
}

for river, country in rivers.items():
    print("The " + river.title() +
          " runs through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe Following counties are included in this data set:")
for country in rivers.values():
    print( "- " + country.title())


