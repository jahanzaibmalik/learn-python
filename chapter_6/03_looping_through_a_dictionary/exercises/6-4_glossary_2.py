glossary = {
    'variable': 'Variables are used to store information.',
    'list': 'A list is a number of items in an ordered or unordered structure.',
    'if-statements': 'An if statement is a conditional statement.',
    'loops': 'A loop is a sequence of instruction.',
    'dictionaries': 'A collection of key-value pairs.',
    'string': 'A sequence of characters.',
    'syntax errors': 'An error in the syntax of a coding',
    'comments': 'A comment allows you to write notes in English.',
    'tuples': 'An immutable list is called a tuple.',
    'boolean expressions': 'A Boolean value is either True or False.'

}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
