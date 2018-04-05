my_pizzas = ['marinara', 'french bred', 'salad']
friend_pizzas = my_pizzas[:]

my_pizzas.append('pepperoni')
friend_pizzas.append('cheese')

print("My favorite pizza are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for value in friend_pizzas:
    print(value)
