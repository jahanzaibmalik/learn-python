# Invite some people to dinner.
guests = ['qasim', 'imran', 'ahsan']

name = guests[0].title()
print("I would like to invite " + name + " for dinner.")

name = guests[1].title()
print("I would like to invite " + name + " for dinner.")

name = guests[2].title()
print("I would like to invite " + name + " for dinner.")

name = guests[0].title()
print("\n " + name + " can't make it to dinner.")

#Qasim can't make it! Let's invite Ali instead.
del guests[0]
guests.insert(0, 'Ali')

# Print the invitation again
name = guests[0].title()
print("\nI would like to invite " + name + " for dinner.")

name = guests[1].title()
print("I would like to invite " + name + " for dinner.")

name = guests[2].title()
print("I would like to invite " + name + " for dinner.")

# We got a bigger table, so Let's add some more people to the list.
print("\nWe got a bigger table!")

guests.insert(0, 'salman')
guests.insert(2, 'siki')
guests.append('malik')

name = guests[0].title()
print("\nI would like to invite " + name + " for dinner.")

name = guests[1].title()
print("\nI would like to invite " + name + " for dinner.")

name = guests[2].title()
print("\nI would like to invite " + name + " for dinner.")

name = guests[3].title()
print("\nI would like to invite " + name + " for dinner.")

name = guests[4].title()
print("\nI would like to invite " + name + " for dinner.")

name = guests[5].title()
print("\nI would like to invite " + name + " for dinner.")

# oh no, the table won't arrive on time!
print("\nSorry we can invite only two people for dinner")
remove_guest = guests.pop()
print("I am sorry " + remove_guest.title() + " I can't invite you for a dinner because tables are short.")

remove_guest = guests.pop()
print("I am sorry " + remove_guest.title() + " I can't invite you for a dinner because tables are short.")

remove_guest = guests.pop()
print("I am sorry " + remove_guest.title() + " I can't invite you for a dinner because tables are short.")

remove_guest = guests.pop()
print("I am sorry " + remove_guest.title() + " I can't invite you for a dinner because tables are short.")

# There should be two people left. Let's invite them.

name = guests[0].title()
print(name + " you are still invite for a dinner everybody except you and ali will not be invitied tonight beacause of table shortage.")

name = guests[1].title()
print(guests[1].title() + " you are still invite for a dinner everybody except you and salman will not be invitied tonight beacause of table shortage.")

# empty oyt the list
del guests[0]
del guests[0]
print(guests)

