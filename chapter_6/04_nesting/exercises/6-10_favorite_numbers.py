favorite_numbers = {
    'ali': [5, 23, 58],
    'shoaib': [4, 6, 62],
    'shahrukh': [9, 10, 18],
    'ahsan': [3, 54, 21],
    'qasim': [52, 87, 91]
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print(" " + str(number))


