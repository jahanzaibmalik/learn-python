# Looping Through All Key-Value Pairs
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(name.title() +
          "'s favorite_language is " +
          language.title() + ".")
