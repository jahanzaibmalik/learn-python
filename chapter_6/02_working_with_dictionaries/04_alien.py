# Modifying Values in a Dictionary
# alien_0 = {'color': 'green'}
# print("The alien is " + str(alien_0['color']) + ".")
#
# alien_0['color'] = 'yellow'
# print("The alien is now " + str(alien_0['color']) + ".")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
