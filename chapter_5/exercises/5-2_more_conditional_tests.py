my_name = 'Jahanzaib'
print("My name is Jahanzaib. I predict True")
print(my_name.lower() == 'jahanzaib')

print("\nMy name is Jahanzaib. I predict False")
print(my_name.lower() != 'jahanzaib')


my_friends = 'ahsan'
print("\nMy friend is ahsan. I predict True.")
print(my_friends == 'ahsan')

print("\nMy friend is not ahsan. I predict False.")
print(my_friends != 'ahsan')


lucky_number = 6
friend_number = 5
print("\nMy lucky number is 6. I predict True.")
print(lucky_number == 6)

print("\nMy lucky number is not 6. I predict False.")
print(lucky_number != 6)

print("\nMy friend's lucky number is 5 and my lucky number is 6. I predict True.")
print(lucky_number == 6 and friend_number == 5)

print("\nMy friend's lucky number is 2 and my lucky number is 6. I predict False.")
print(lucky_number == 6 and friend_number == 2)

print("\nMy friend's lucky number is 2 or my lucky number is 6. I predict True.")
print(lucky_number == 6 or friend_number == 2)

print("\nMy friend's lucky number is greater than or equals to 6 or my lucky number is greater than or equals to 7. I predict False.")
print(lucky_number >= 7 or friend_number >= 6)

print("\nMy friend's lucky number is less than or equals to 6 or my lucky number is less than or equals to 7. I predict True.")
print(lucky_number <= 7 or friend_number <= 6)

print("\nMy friend's lucky number is less than or equals to 4 or my lucky number is less than or equals to 4. I predict False.")
print(lucky_number <= 4 or friend_number <= 4)

favorite_games = ['mario', 'cadillac and dinosoure', 'final fight', 'street fighter']

print("'\nmario in favorite games? I predict is True'")
print('mario' in favorite_games)

print('\nFinal Fight not in favorite games? I predict is False')
print('final fight' not in favorite_games)