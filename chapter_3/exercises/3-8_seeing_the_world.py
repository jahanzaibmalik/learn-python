desire_places = ['madina', 'lahore', 'baghdad', 'karbala', 'iran']
print("Original list:")
print(desire_places)

print("\nTemporary sorted list:")
print(sorted(desire_places))

print("\nOriginal list:")
print(desire_places)

print("\nTemporary sorted reverse mode:")
print(sorted(desire_places, reverse=True))

print("\nOriginal list:")
print(desire_places)

print("\nExact reverse list")
desire_places.reverse()

print("\nOriginal list:")
print(desire_places)

print("\nReverse again:")
desire_places.reverse()

print("\nOriginal list:")
print(desire_places)

print("\nPermanently sorted list:")
desire_places.sort()

print("\nPermanently changed llist:")
print(desire_places)

print("\nPermanently reverse sorted list:")
desire_places.sort(reverse=True)
print(desire_places)