# user_0 = {
#     'username': 'shahrukh',
#     'first': 'jahanzaib',
#     'last': 'malik'
# }
#
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# for name in favorite_languages.keys():
#     print(name.title())


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print("    HI " + name.title() +
#               ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# if 'eric' not in favorite_languages.keys():
#     print("Eric, please take our poll!")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


