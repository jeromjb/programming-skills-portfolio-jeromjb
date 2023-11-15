'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.'''


glossary = {'variable': 'A named storage location for holding data',
            'function': 'A code that performs specific task',
            'list': 'An ordered collection of items',
            'dictionary': 'A collection of key-value pairs',
            'Tuple': 'An ordered, immutable sequence of elements',
            'Boolean':'A data that express values as True or False',
            'String': 'Statements surrounded with one or more quotations'}

for word, meaning in glossary.items():
    print (f"{word}:\n{meaning}\n")