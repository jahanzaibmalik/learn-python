guests = ['qasim', 'imran', 'ahsan']

print("I would like to invite " + guests[0].title() + " for dinner.")
print("I would like to invite " + guests[1].title() + " for dinner.")
print("I would like to invite " + guests[2].title() + " for dinner.")

print("\n " + guests[0].title() + " can't make a dinner with us.")
guests[0] = "ali"

print("\nI would like to invite " + guests[0].title() + " for dinner.")
print("I would like to invite " + guests[1].title() + " for dinner.")
print("I would like to invite " + guests[2].title() + " for dinner.")

print("\n" + guests[0].title() + " I found the bigger dinner table so more firends will be coming.")
print(guests[1].title() + " I found the bigger dinner table so more firends will be coming.")
print(guests[2].title() + " I found the bigger dinner table so more firends will be coming.")

guests.insert(0, 'salman')
guests.insert(2, 'siki')
guests.append('malik')

print("\nI would like to invite " + guests[0].title() + " for dinner.")
print("I would like to invite " + guests[1].title() + " for dinner.")
print("I would like to invite " + guests[2].title() + " for dinner.")
print("I would like to invite " + guests[4].title() + " for dinner.")
print("I would like to invite " + guests[5].title() + " for dinner.")

