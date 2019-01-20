alphabet = 'abcdefghijklmnopqrstuvwxyz'

# user inputs number to encrypt key
key = int(input('Enter key number: '))
print('Key number: ', key)

character = input('Enter a character to encrypt: ')
# will find the numerical position of the character submitted
position = alphabet.find(character)
print('The position of character: ', position)

# adds 5 to numerical position and after 26 it goes back to 0
new_position = (position + key) % 26
print('New position: ', new_position)

# prints out new letter after numerical position is identified
new_character = alphabet[new_position]
print('New character: ', new_character)

# Caesar cipher swaps letters around by using the numerical key inputted to create a new character 
