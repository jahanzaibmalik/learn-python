favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(name.title() +
          "'s favorite language is " + language.title() + ".")

print("\n")

coders = ['jen', 'phil', 'qasim', 'mehmood', 'imran']
for coder in coders:
    if coder in favorite_languages.keys():
        print(coder.title() + ", thanks for taking the poll!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
