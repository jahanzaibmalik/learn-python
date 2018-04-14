# A List of Dictionaries
# aliens = []
# for value in range(30):
#     new_alien = {'speed': 'slow', 'color': 'green', 'points': 5}
#     aliens.append(new_alien)
#
# for alien in aliens[:5]:
#     print(alien)
#
# print("...")
# print("\nTotal number of aliens: " + str(len(aliens)))


aliens = []
for alien_number in range(30):
    new_alien = {'speed': 'slow', 'color': 'green', 'points': 5}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    # elif alien['color'] == 'yellow':
    #     alien['color'] = 'red'
    #     alien['speed'] = 'fast'
    #     alien['points'] = 15

for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)

print("...")
print("\nTotal number of aliens: " + str(len(aliens)))

