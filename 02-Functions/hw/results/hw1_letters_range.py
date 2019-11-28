def letters_range(*args, **kwargs):
    """ Returning list of letters from latin alphabet:
    - beginning with start letter (default is 'a')
    - ending with stop letter (no default)
    - with a step (default is 0)
    Opportunity to translate the original latin alphabet letter
    into random symbols by providing a dictionary of translation as
    a function argument.
    """
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    if kwargs:
    	for letter in kwargs:
    		alphabet[alphabet.index(letter)] = str(kwargs[letter])
    if len(args) == 1:
        start = 'a'
        stop = args[0]
        step = 1
    elif len(args) == 2 and type(args[1]) == int:
        start = 'a'
        stop, step = args[0], args[1]
    elif len(args) == 2 and type(args[1]) != int:
        start, stop = args[0], args[1]
        step = 1
    elif len(args) == 3:
    	start, stop, step = args[0], args[1], args[2]
    result = alphabet[alphabet.index(start):alphabet.index(stop):step]
    return result

# examples
print(letters_range('b', 'w', 2))
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']
print(letters_range('g'))
# ['a', 'b', 'c', 'd', 'e', 'f']
print(letters_range('g', 'p'))
# ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
print(letters_range('g', 'p', **{'l': 7, 'o': 0}))
# ['g', 'h', 'i', 'j', 'k', '7', 'm', 'n', '0']
print(letters_range('p', 'g', -2))
# ['p', 'n', 'l', 'j', 'h']
print(letters_range('a'))
# []